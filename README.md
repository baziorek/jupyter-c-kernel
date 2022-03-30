# C++ kernel for Jupyter (not ready - I'm playing with its, but it is not working, WORK IN PROGRESS)

I would like to use Jupyter for C++ programming in education (many simple programs). Unfortunately for C++ all kernels are using Cling, which is not C++, but C++-like interpreted language. For education it is really hard to use Cling. Thats why I decided that another kernel for C++ would be really usefull, but the kernel should send the program to normal C++ compiler.

That's why I've forked [https://github.com/XaverKlemenschits/jupyter-c-kernel](XaverKlemenschits/jupyter-c-kernel) and I'm trying to make everything working for C++.

My plan is not to just replace commands from `gcc` to `g++` but for security reason to use [CoLiRu](https://coliru.stacked-crooked.com/) and [its API](https://docs.google.com/document/d/18md3rLdgD9f5Wro3i7YYopJBFb_6MPCO8-0ihtxHoyM/edit#heading=h.3md6zepla0fj) to get results of compilation and running of code.

# If You have time You can help me to finish the project. I'm quite busy person:).

My plan is to:
* handle streams `cout`, `cin`
* support different compilers (as CoLiRu supports)
* support for many C++ standards (as CoLiRu supports)
* using different compiler and warning flags (e.g. `-Wall`)

## Manual installation

Works only on Linux and OS X. Windows is not supported yet. If you want to use this project on Windows, please use Docker.

* Make sure you have the following requirements installed:
  * g++
  * jupyter
  * python 3
  * pip

### Step-by-step

```bash
git clone https://github.com/baziorek/jupyter-cpp-kernel.git
cd jupyter-cpp-kernel
pip3 install -e .  # for system install: sudo install .
cd jupyter-cpp-kernel && install_c_kernel --user # for sys install: sudo install_c_kernel
# now you can start the notebook
jupyter notebook
```

# Below is text rest from [https://github.com/XaverKlemenschits/jupyter-c-kernel](XaverKlemenschits/jupyter-c-kernel), please ignore:

## Example of notebook

![Example of notebook](example-notebook.png?raw=true "Example of notebook")

## Custom compilation flags

You can use custom compilation flags like so:

![Custom compulation flag](custom_flags.png?raw=true "Example of notebook using custom compilation flags")

Here, the `-lm` flag is passed so you can use the math library.

## Contributing

The docker image installs the kernel in editable mode, meaning that you can
change the code in real-time in Docker. For that, just run the docker box like
that:

```bash
git clone https://github.com/XaverKlemenschits/jupyter-c-kernel.git
cd jupyter-c-kernel
docker build -t myName/jupyter .
docker run -v $(pwd):/tmp/jupyter_c_kernel/ -p 8888:8888 myName/jupyter
```

This clones the source, run the kernel, and binds the current folder (the one
you just cloned) to the corresponding folder in Docker.
Now, if you change the source, it will be reflected in [http://localhost:8888](http://localhost:8888)
instantly. Do not forget to click "restart" the kernel on the page as it does
not auto-restart.

## License

[MIT](LICENSE.txt)
