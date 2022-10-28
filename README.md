[![FCB-Python-autograding](../../actions/workflows/fcb_autograding.yml/badge.svg)](../../actions?query=workflow%3AFCB-Python-autograding)

# Assignment 5 - FCB 2022
### Deadline: 04/11/2022 - 23:59

## Submission procedure

This assignment has to be submitted using GitHub Classroom. This
means that you should have cloned the GitHub repo of this assignment from
the organization account for FCB in the academic year 2022-23 at
[https://github.com/funcompbio2022](https://github.com/funcompbio2022)
using the submission link provided at the FCB Moodle site.

Once you have cloned the GitHub repo which has `assignment-5` and your
GitHub username as repo name, then you can work on it in your local disk
and _push_ your changes whenever you like, but make sure that you have pushed
the last version of your assignment before the deadline. There is no
_submit_ button or any other specific submission procedure or action than
just pushing your changes to you GitHub assignment repo. When correcting the
assignment, the version available at the deadline will be retrieved. If the
first version available is posterior to the deadline, then the mark of the
assignment will have a penalty.

To complete your submission (see rubric below) please **agree to the following
academic integrity statement** by editing this README file and placing the
letter `X` between the squared brackets preceding the statement:

- [] The work here submitted as been entirely developed by myself and is the
  result of my own work.

## Description

[Huntington's disease](https://en.wikipedia.org/wiki/Huntington%27s_disease) is
an hereditary genetic disorder, caused by an expansion of consecutive repetitions
of the `CAG` tri-nucleotide in a gene named after the disease, the
[Huntingtin (_HTT_)](https://www.ncbi.nlm.nih.gov/gene/3064) gene. Unaffected
individuals usually have no more than 30 consecutive repetitions of the `CAG`
tri-nucleotide in the _HTT_ gene, while affected individuals usually have more
than 37.

The goal of this assignment is to **implement a program in Python that given the
name of a FASTA file containing the DNA sequence of the _HTT_ gene of an
individual, it calculates the maximum number of consecutive `CAG` tri-nucleotide
repetitions found in the DNA sequence**. It is important that the program does
*not* ask for the name of the FASTA file, but instead it takes it as the first
argument from the Unix shell command-line call, i.e., by doing something like:

```
$ python src/cagrepmax.py <filename>
```

This assignment incorporates an autograding feature using a so-called
[GitHub Actions Worflow](https://github.com/features/actions), which will
help you to automatically test whether your Python program is
correctly working after every _push_. More concretely, a few minutes after
you _pushed_ your changes to your remote GitHub repo, the badge labeled
`FCB-Python-autograding` on top of this README file will be red and display
the message `failing` if the autograding has not been successful, and
green with the message `passing` otherwise. You may click on the badge to
look at the output of the autograding tests to understand why it has failed,
if that was the case. This feature provides you with
[formative assessment](https://en.wikipedia.org/wiki/Formative_assessment)
and to work with it you need to edit your program in the existing file
`src/cagrepmax.py` and leave the rest of the files and directory
structure intact. The file `src/cagrepmax.py` is a template that
contains instructions written as comments, indicating where should you
edit your code.

The template repo and autograding feature will test your program with DNA
sequences of the [Huntingtin (_HTT_)](https://www.ncbi.nlm.nih.gov/gene/3064)
gene for six simulated (i.e., not real) individuals, where three of them are
affected by
[Huntington's disease](https://en.wikipedia.org/wiki/Huntington%27s_disease)
and the other three are healthy. These DNA sequences are stored as FASTA files
in the directory called `FASTA` and their names contain the maximum number of
`CAG` consecutive repeats found in the stored DNA sequence. For example, to
test in your own computer whether your Python program works fine with one of
those sequences, first change your current working directory to the top
directory of the your local copy of this GitHub repo and type:

```
$ python src/cagrepmax.py FASTA/affected_individual1_40_CAGs.fa
```

If the program works as expected, for this particular example affected by
the disease, it should output the number 40, as indicated in the FASTA filename.
For the autograding tool to give you the correct feedback, it is important that
your program **only outputs a number**. You should make sure that your program
gives the expected result with every of the sequence files you can find in the
`FASTA` directory.

Your assignment repo should have the following files:

  1. This `README.md` file.
  2. The `src` directory with the initial files of the assignment repo.
  3. The `tests` directory with the initial files of the assignment repo.
  4. The `FASTA` directory with the initial files of the assignment repo.

Eventually, you may encounter that Python automatically creates a directory called
`__pycache__`, you may ignore that directory since this template is already
prepared to ignore that directory by including it into a `.gitignore` file that
informs Git to avoid putting certain files under version control. In any case,
**you should only be editing the file `src/cagrepmax.py` and `README.md` to agree
to the academic integrity statement**.

## Evaluation rubric

The rubric to evaluate this assignment consists of the following items:

  * Did you agree to the academic integrity statement?
  * Does the assignment contain the required files?
  * Does the Python program `src/cagrepmax.py` runs without errors?
  * Does the Python program `src/cagrepmax.py` correctly calculates the maximum
    number of consecutive `CAG` tri-nucleotide repetitions found in a DNA sequence?
  * Does the Python program `src/cagrepmax.py` passes all autograding tests?
