#!/usr/bin/perl
use strict;
use warnings;

if (@ARGV < 2 || @ARGV > 3) {
    die "Usage: trec_eval [-q] <qrel_file> <trec_file>\n";
}

my $print_all_queries = 0;

if (@ARGV == 3) {
    shift;
    $print_all_queries = 1;
}

my $qrel_file = shift;
my $trec_file = shift;

open(QREL, $qrel_file) or die "Cannot open $qrel_file: $!\n";
my @data = split(/\s+/, do { local $/; <QREL> });
close(QREL);

my (%qrel, %num_rel);

while (@data) {
    my ($topic, $dummy, $doc_id, $rel) = splice(@data, 0, 4);
    $qrel{$topic}{$doc_id} = $rel;
    $num_rel{$topic} += $rel;
}

open(TREC, $trec_file) or die "Cannot open $trec_file: $!\n";
@data = split(/\s+/, do { local $/; <TREC> });
close(TREC);

my %trec;

while (@data) {
    my ($topic, $dummy, $doc_id, $dummy2, $score, $dummy3) = splice(@data, 0, 6);
    $trec{$topic}{$doc_id} = $score;
}

my @recalls = (0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0);
my @cutoffs = (5,10,15,20,30,100,200,500,1000);

my ($tot_num_ret, $tot_num_rel, $tot_num_rel_ret) = (0,0,0);
my ($sum_avg_prec, $sum_r_prec) = (0,0);
my @sum_prec_at_cutoffs = (0) x @cutoffs;
my @sum_prec_at_recalls = (0) x @recalls;

my $num_topics = 0;

foreach my $topic (keys %trec) {

    next if !defined $num_rel{$topic} || $num_rel{$topic} == 0;

    my $href = $trec{$topic};

    my @prec_list = (0) x 1001;
    my @rec_list  = (0) x 1001;

    my ($num_ret, $num_rel_ret, $sum_prec) = (0,0,0);

    foreach my $doc_id (sort {
        ($href->{$b} <=> $href->{$a}) || ($a cmp $b)
    } keys %$href) {

        $num_ret++;

        my $rel = $qrel{$topic}{$doc_id} // 0;

        if ($rel) {
            $sum_prec += $rel * (1 + $num_rel_ret) / $num_ret;
            $num_rel_ret += $rel;
        }

        $prec_list[$num_ret] = $num_rel_ret / $num_ret;
        $rec_list[$num_ret]  = $num_rel_ret / $num_rel{$topic};

        last if $num_ret >= 1000;
    }

    my $avg_prec = ($num_rel{$topic} > 0)
        ? $sum_prec / $num_rel{$topic}
        : 0;

    my $final_recall = $num_rel_ret / $num_rel{$topic};

    for (my $i = $num_ret+1; $i <= 1000; $i++) {
        $prec_list[$i] = $num_ret ? $num_rel_ret / $i : 0;
        $rec_list[$i]  = $final_recall;
    }

    my @prec_at_cutoffs;
    foreach my $c (@cutoffs) {
        push @prec_at_cutoffs, $prec_list[$c] // 0;
    }

    my $r_prec = ($num_rel{$topic} > 0)
        ? $num_rel_ret / $num_rel{$topic}
        : 0;

    my $max_prec = 0;
    for (my $i = 1000; $i >= 1; $i--) {
        $max_prec = $prec_list[$i] if $prec_list[$i] > $max_prec;
        $prec_list[$i] = $max_prec;
    }

    my @prec_at_recalls;
    my $i = 1;

    foreach my $rec (@recalls) {
        while ($i <= 1000 && $rec_list[$i] < $rec) {
            $i++;
        }

        push @prec_at_recalls,
            ($i <= 1000) ? $prec_list[$i] : 0;
    }

    $num_topics++;

    $tot_num_ret     += $num_ret;
    $tot_num_rel     += $num_rel{$topic};
    $tot_num_rel_ret += $num_rel_ret;

    for my $i (0..$#cutoffs) {
        $sum_prec_at_cutoffs[$i] += $prec_at_cutoffs[$i];
    }

    for my $i (0..$#recalls) {
        $sum_prec_at_recalls[$i] += $prec_at_recalls[$i];
    }

    $sum_avg_prec += $avg_prec;
    $sum_r_prec   += $r_prec;

    if ($print_all_queries) {
        print "$topic $avg_prec $r_prec\n";
    }
}

for my $i (0..$#cutoffs) {
    $sum_prec_at_cutoffs[$i] /= $num_topics if $num_topics;
}

for my $i (0..$#recalls) {
    $sum_prec_at_recalls[$i] /= $num_topics if $num_topics;
}

my $MAP = $num_topics ? $sum_avg_prec / $num_topics : 0;
my $avg_r_prec = $num_topics ? $sum_r_prec / $num_topics : 0;

print "\nMAP: $MAP\n";
print "R-Precision: $avg_r_prec\n";