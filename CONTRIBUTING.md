# Contributing to ignition-api

We follow a simple model to make contributing as straightforward as possible. These guidelines allow us to streamline the development process and achieve greater transparency.

## Code of Conduct

Help us keep **ignition-api** open and inclusive. Please read and follow our [Code of Conduct](https://github.com/ignition-api/.github/blob/main/CODE_OF_CONDUCT.md).

## Got a question?

Please join us on or [Discussions](https://github.com/ignition-api/discussions/discussions).

## Found a bug?

If you find a bug or if something is missing in the source code, you can help us by submitting an issue, or even better, you can [submit a Pull Request](#pull-requests) with a fix.

## Getting ready to contribute

In **ignition-api** we rely on Python 2.7.18 for development, and Python 3.10 to run tests and style checks with `pre-commit` and `tox`.

### Setting up your local environment

1. Install Python 2.7.18 and the latest 3.10 release
1. Install the required packages for development you may run the following command:

    ```sh
    python2 -m pip install --requirement requirements.txt
    ```

1. Install Python 3 tools

    1. [`pre-commit`](https://pre-commit.com/)

        ```sh
        python3 -m pip install pre-commit
        ```

        1. Install the git hook scripts

            ```sh
            pre-commit install
            ```

    1. [`tox`](https://tox.wiki/)

        ```sh
        python3 -m pip install tox
        ```

## Pull Requests

In **ignition-api** we use the [GitHub flow](https://guides.github.com/introduction/flow/) as main versioning workflow.

1. Fork the repository
1. Create a new branch from **main** for each feature, fix or improvement, using the following naming convention:
    1. `feat/scope/feature-name` when introducing a new feature
    1. `fix/scope/fix-name` when fixing an existing issue
    1. `docs/change` for documentation changes
    1. `chore/chore-desc` for miscellaneous changes
1. Make sure to run `pre-commit` and `tox`
1. Add your commits to the branch following our [Commit Message Format](#commit-message-format)
1. Send a pull request from each feature branch to the **main** branch

It is very important to separate new features or improvements into separate feature branches, and to send a pull request for each branch.

This allows us to review and pull in new features or improvements individually.

## Coding style

We use the [Black code style](https://github.com/psf/black/blob/main/docs/the_black_code_style/index.rst), but also rely on other tools.

## Commit Message Format

We have very precise rules over how our Git commit messages must be formatted.
This format leads to **easier to read commit history**.

Each commit message consists of a **header**, a **body**, and a **footer**, trying to adhere to the ["50/72 rule"](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html).

```text
<header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

The `header` is mandatory and must conform to the [Conventional Commits specification](https://conventionalcommits.org/).
Additionally, we recommend trying to keep the `header` to a maximum of 50 characters.

The `body` is mandatory for all commits except for those of type "docs".
When the body is present it should be wrapped at 72 characters.

The `footer` is optional. The [Commit Message Footer](#commit-message-footer) format describes what the footer is used for and the structure it must have.

## Commit message header

```text
<type>(<scope>): <summary>
```

The `<type>` and `<summary>` fields are mandatory, the `(<scope>)` field is optional.

### Type

Must be one of the following:

* **build**: Changes that affect the build system or external dependencies (example scope: `deps`, `pip`)
* **chore**: Other changes that don't modify src or test files (example scopes: `release`)
* **ci**: Changes to our CI configuration files and scripts (example scope: `pip`)
* **docs**: Documentation only changes
* **feat**: A new feature (example scopes: `ia`, `java`, `javax`, `org`, `system`, `thecesrom`)
* **fix**: A bug fix (example scopes: same as **feat**)
* **perf**: A code change that improves performance (example scopes: same as **feat**)
* **refactor**: A code change that neither fixes a bug nor adds a feature (example scopes: same as **feat**)
* **revert**: Reverts a previous commit
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, etc.)
* **test**: Adding missing tests or correcting existing tests

### Scope

The `scope` should be the name of the Python package affected.

The following is the list of supported scopes:

* **ia**: for changes to the `com.inductiveautomation` package
* **java**: for changes to the `java` package
* **javax**: for changes to the `javax` package
* **org**: for changes to the `org` package
* **pip**: for changes to Python Packaging files (`pyproject.toml`, `setup.cfg`, `setup.py`)
* **system**: for changes to the `system` package
* **thecesrom**: for changes to the `dev.thecesrom` package

There are currently a few exceptions to the "use package name" rule:

* **deps**: for updating dependencies for our CI scripts. This is mainly used by `dependabot` and `pre-commit.ci`
* **pip**: for changes to `setup.[cfg|py]`, or the package publishing workflow
* **release**: used for creating a new release
* none/empty string: useful for changes that are done across all packages (e.g. `style: use black style`) and for docs changes that are not related to a specific package (e.g. `docs: fix typo in README`).

## Summary

Use the summary field to provide a succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize the first letter
* no dot (.) at the end

Example Conventional Commit message:

```text
refactor(ia): improve Version comparison logic
```

## Commit Message Footer

The footer can contain information about breaking changes and deprecations and is also the place to reference GitHub issues, and other PRs that this commit closes or is related to.
For example:

```text
BREAKING CHANGE: <breaking change summary>
<BLANK LINE>
<breaking change description + migration instructions>
<BLANK LINE>
<BLANK LINE>
Fixes #<issue number>
```

or

```text
DEPRECATED: <what is deprecated>
<BLANK LINE>
<deprecation description + recommended update path>
<BLANK LINE>
<BLANK LINE>
Closes #<pr number>
```

Breaking Change section should start with the phrase "BREAKING CHANGE: " followed by a summary of the breaking change, a blank line, and a detailed description of the breaking change that also includes migration instructions.

Similarly, a Deprecation section should start with "DEPRECATED: " followed by a short description of what is deprecated, a blank line, and a detailed description of the deprecation that also mentions the recommended update path.

## Revert commits

If the commit reverts a previous commit, it should begin with `revert:`, followed by the header of the reverted commit.

The content of the commit message body should contain:

* information about the SHA of the commit being reverted in the following format: `This reverts commit <SHA>`,
* a clear description of the reason for reverting the commit message.

Example:

```text
revert(ci): remove condition from job

Refs: 2a50de4
```
