import os
import subprocess
import click


def extract_integer_from_filename(filename):
    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)
    integer_part = name.split("_")[-1]
    try:
        return int(integer_part)
    except ValueError:
        return None


filename = "/Users/vaibhavblayer/10xphysics/iitjee-papers/2023/paper-1/paper/problem_1.tex"
integer_part = extract_integer_from_filename(filename)
print(integer_part)


def make_folder_with_basename(filename):
    base = os.path.basename(filename)
    name, ext = os.path.splitext(base)
    folder_name = os.path.dirname(filename) + "/" + "problems" + "/" + name
    os.makedirs(folder_name, exist_ok=True)
    return folder_name


make_folder_with_basename(filename)


def make_file_in_folder(folder_name, n):
    file_name = folder_name + "/main.tex"
    with open(file_name, "w") as file:
        file.write(r"\documentclass{article}" + "\n")
        file.write(r"\usepackage{v-test-paper}" + "\n")
        file.write(
            r"\newenvironment{solution}{\par\noindent\color{red!85!black}$\Rightarrow$\vspace{0em}}{}" + "\n")
        file.write(
            r"\title{\textsc{JEE Advanced 2023 Paper-I\\Physics}}" + "\n")
        file.write(r"\begin{document}" + "\n")
        file.write(r"\maketitle" + "\n")
        file.write(
            r"\begin{enumerate}\setcounter{enumi}{" + f"{n-1}" + r"}" + "\n")
        file.write(r"\input{../../" + f"problem_{n}.tex" + r"}" + "\n")
        file.write(r"\end{enumerate}" + "\n")
        file.write(r"\end{document}")


make_file_in_folder(make_folder_with_basename(filename),
                    extract_integer_from_filename(filename))


def run_subprocess_with_verbose(folder_name):
    subprocess.call(["pdflatex", "-interaction=nonstopmode",
                    "-file-line-error", "-halt-on-error", "main.tex"], cwd=folder_name)


run_subprocess_with_verbose(make_folder_with_basename(filename))


@click.command()
@click.argument('filename')
def main(filename):
    integer_part = extract_integer_from_filename(filename)
    folder_name = make_folder_with_basename(filename)
    make_file_in_folder(folder_name, integer_part)
    run_subprocess_with_verbose(folder_name)


if __name__ == '__main__':
    main()
