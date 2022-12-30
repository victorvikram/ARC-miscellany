# solution-first-place-pruned
Contains all the source files for my modified version of the first-place solution. To run, exectue `python safe_run.py <directory>` where the `<directory>` is the dataset directory *relative to* the `solution-first-place-pruned/dataset` folder. That is, if have a directory called `solution-first-place-pruned/dataset/arc-problems` that contains ARC json files, you would call `python safe_run.py arc-problems`. 

The output is a submission file which can be scored using `score_submission.py`.

There are some hangups: for example, the code only seems to work on linux. See (the full forked repository)[https://github.com/victorvikram/ARC-icecuber] for more details.

# solution-third-place-pruned
This contains a single notebook that runs the third place solution end-to-end. Follow the instructions in the first cell to run it. The output is similarly a submission file, `submission.csv`, that can be scored using `score_submission.py`.

# score_submission.py
This script scores submission files. See the comments in the file for how to use it.

# draw-arc.ipynb
This notebook takes a json ARC file as input and outputs (what I believe to be) a nice-looking depiction of the problem. See the first cell of the notebook for instructions.

# Other repositories
* For an ARC editor, go to (ARC site)[https://github.com/victorvikram/arc-site].
* To modify the ARC editor, go to (ARC app)[https://github.com/victorvikram/arc-app].
* For the full modified version of the first place ARC solution, go to (ARC icecuber)[https://github.com/victorvikram/ARC-icecuber]
