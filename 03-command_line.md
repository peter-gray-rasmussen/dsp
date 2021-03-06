# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

```
pwd print working directory
hostname my computer's network name (p-mac)
mkdir make directory
cd change directory
ls list directory
rmdir remove directory
pushd push directory
popd pop directory
cp copy a file or directory
mv move a file or directory
less page through a file
cat print the whole file
xargs executes arguments
find find files
grep find things inside files
man read a manual page
apropos find what man page is appropriate
env look at your environment
echo print some arguments
export export/set a new environment variable
exit exit the shell
sudo become super user
chmod change permission modifiers
chown change ownership
```

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

```
ls prints the files and directories in the working directory
ls -a also prints hidden files
ls -l prints files and directories as records each with six columns
ls -lh prints files in human-readable format in column form
I can imagine ls -lt is useful since it prints contents in column form sorted by modification time.
The flag -a that prints hidden files is nice as well, and could be used with -t to print contents including hidden files sorted by modification time.
```

---


---

What does `xargs` do? Give an example of how to use it.

```
xargs is a command used with find and grep to divide a big list of arguments in to a small list received from standard input (http://javarevisited.blogspot.com/2012/06/10-xargs-command-example-in-linux-unix.html)

Example is using xargs with find and grep to print out queried keywords within queried filenames. For instance, in my temp directory I can do the following to print out instances of the word "old" (case insensitive) within all text files: find . -name "*.txt" | xargs grep -i "old"
```

---

