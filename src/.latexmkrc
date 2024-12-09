use Cwd 'getcwd';
use File::Basename;
my $path = getcwd;
if ($jobname == 'main') {
    $jobname = basename($path);
}

$lualatex = 'texfot lualatex %O -halt-on-error -file-line-error %S';
# $lualatex = 'lualatex %O -halt-on-error -file-line-error %S';
$out_dir = '../../pdf/' . basename($path)
