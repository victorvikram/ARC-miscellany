# This repository
## solution-first-place-pruned
Contains all the source files for my modified version of the first-place solution. To run, exectue `python safe_run.py <directory>` where the `<directory>` is the dataset directory *relative to* the `solution-first-place-pruned/dataset` folder. That is, if have a directory called `solution-first-place-pruned/dataset/arc-problems` that contains ARC json files, you would call `python safe_run.py arc-problems`. 

The output is a submission file which can be scored using `score_submission.py`.

There are some hangups: for example, the code only seems to work on linux. See [the full forked repository](https://github.com/victorvikram/ARC-icecuber) for more details.

## solution-second-place-pruned
This contains a single notebook that runs the third place solution end-to-end. Follow the instructions in the first cell to run it. The output is similarly a submission file, `submission.csv`, that can be scored using `score_submission.py`.

## solution-third-place-pruned
The final copy of this notebook is titled `third-place-end-to-end.ipnyb` (no indices). Follow the instructions in the first cell to run it. The output is similarly a submission file, `submission.csv`, that can be scored using `score_submission.py`.

## score_submission.py
This script scores submission files. See the comments in the file for how to use it.

## draw-arc.ipynb
This notebook takes a json ARC file as input and outputs (what I believe to be) a nice-looking depiction of the problem. See the first cell of the notebook for instructions.

## arc-datasets
These are common sets of ARC problems that I have been using

## example-submissions
These are example submission files of the form that were submitted the the ARC Kaggle competition

## experiment-scores
These are results of experiments running various solvers on datasets.

# Other resources
* [Ensemble solver, hosted on Kaggle](https://www.kaggle.com/code/vicviod/arc-late-submission-1st-and-2nd-place-ensemble)
* For an ARC editor, go to [ARC site](https://github.com/victorvikram/arc-site).
* To modify the ARC editor, go to [ARC app](https://github.com/victorvikram/arc-app).
* For the full modified version of the first place ARC solution, go to [ARC icecuber](https://github.com/victorvikram/ARC-icecuber)
* [The original ARC dataset](https://github.com/fchollet/ARC)
* [First place ARC solution repository](https://github.com/top-quarks/ARC-solution)
* [Third place ARC solution repository](https://github.com/alejandrodemiquel/ARC_Kaggle)

