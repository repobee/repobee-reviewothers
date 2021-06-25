# repobee-reviewothers
A plugin to allow some students to review others, such as for peer grading

A [RepoBee](https://github.com/repobee/repobee) plugin that allows support for some students in the class to review all of the others. The intended use case is when a small set of students in the class have been selected as peer graders, where they grade the assignments of all of the other students in the class.

## Install
Use RepoBee's plugin manager to install.

```bash
$ repobee plugin install
```

## Usage
When active, the `reviewothers` plugin adds the `--reviewothers-grader` option to the `review` command. The command works with all of the options that `review` normally permits. The change in behavior is that normally, the review command randomly assigns students to review each other; instead, this assigns all students (specified by either the `-s` or `--sf` command like flags) to be reviewed by the student specified by the `--reviewothers-grader` option.

If you wish to assign multiple reviewers (i.e., if you have multiple peer graders), then just issue the command multiple times. For example:


```
repobee -a assignment1 --sf students.txt --reviewothers-grader alice
repobee -a assignment1 --sf students.txt --reviewothers-grader bob
```

# License
See [LICENSE](LICENSE) for details.
