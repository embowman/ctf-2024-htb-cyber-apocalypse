## Time KORP

This one is thanks to John Hammond.

I perused the provided files, saw the exec method in
[TimeModel.php](./web_timekorp/challenge/models/TimeModel.php),
and searched for php command injection.
I simply implemented what he showed and made sure to cat the flag at the path shown in the
[Dockerfile](./web_timekorp/Dockerfile)