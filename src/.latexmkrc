use Cwd;
use File::Basename;

# カレントディレクトリ名を取得
my $curr_path = getcwd();
my $curr_dir_name = basename($curr_path);

# 親ディレクトリ名を取得
my $parent_path = dirname($curr_path);
my $parent_dir_name = basename($parent_path);

# ファイル名の接頭辞・接尾辞を指定
my $jobname_prefix = $parent_dir_name;
my $jobname_postfix = $curr_dir_name;

# main ファイルの場合は接尾辞を省略
if ($jobname_postfix eq "main") {
    $jobname = $jobname_prefix;
} else {
    $jobname = $jobname_prefix."-".$jobname_postfix;
}

# 出力ディレクトリ
$out_dir = '../../../pdf/' . $jobname_prefix;

$lualatex = "lualatex %O -halt-on-error -file-line-error %S";

$makeindex = 'upmendex -s jpbase -l %O -o %D %S';
