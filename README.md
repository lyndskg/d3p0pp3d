<a name="top"></a>
<h1 align="center">d3p0pp3d</h1> 
<h4 align = "center"><ins><em><strong>* welcome to the depop sharing app * </em></strong></ins></h4>

<p align="center">
  <a href="https://www.linkedin.com/in/lyndsey791/">LinkedIn</a>  |  <a href="https://www.sorry-this-site-doesnt-exist-yet./">Website</a>  |     <a href="https://github.com/lyndskg/">GitHub</a>  |  <a href="#contact">Contact Info</a>
</p>


## Project Overview
This script is designed for users with a [seller account on Depop marketplace](https://depop.com).

### <ins>Objectives</ins>:

`d3p0pp3d`'s primary functionalities include: 
> - automated sharing of the listings for every item in your closet with all subscribers, or
> - automated sharing of all the listings of another Depop account. 

&nbsp;

Once the script is executed, it will share the requested listings every 120 minutes. 

<h4><strong></strong><ins>Note</ins>:</strong> <em>You can edit the timing and other options if you desire.</em></h4>

------

&nbsp;

## Let the Share War Begin

### <ins>Prerequisites</ins>
> - `Python`: v.*3.5+*
> - `Firefox`: v.*69.0.1+*
> - [`Selenium`](http://selenium-python.readthedocs.io): v.*4.11.0+*
>   - __<ins>Note</ins>:__ For Safari, `Selenium` must be v.*5+*
> - [`Numpy`](https://numpy.org/): v.*1.25.2+*
> - `webdriver_manager`: v.*4.0.0+*
> - `pyautogui`: v.*0.9.54+*
> - `logging`: v.*0.5.1.2+*

&nbsp;

To install `Python3` requirements, you may run `pip install -r requirements.txt`. 



You will also need a recent version of `Firefox` (or another webdriver of your choice). 
> - If using `Firefox`, you will also likely need to install `GeckoDriverManager`, which on macOS can be accomplished using [Homebrew](https://brew.sh/) with the command `brew install geckodriver` in terminal.
> - If using `Edge`, you will need to install `EdgeChromiumDriverManager`.


<p align="right"><a href="#top">(back to top)</a></p>

------

&nbsp;

## Setup

### <ins>Git Clone</ins>:

First clone the repository in terminal:
* `git clone https://github.com/lyndskg/d3popp3d`

Change directories to enter the local repository:
* `cd d3p0pp3d`

<p align="right"><a href="#top">(back to top)</a></p>


### <ins>User Credentials</ins>:

You will need to create a `credentials.py` file.


It is recommended to simply edit the `example_credentials.py` file and rename it.

```python3
depop_username = "depopusername"
depop_password = "depoppassword"
```

Edit the text in quotes to your actual username and password. Save the file and rename it `credentials.py`. 
> Assuming you are in the repo directory, the `bash` command would be `mv example_credentials.py credentials.py` .

&nbsp;


<p align="right"><a href="#top">(back to top)</a></p>

### <ins>Firefox and Other Web Drivers</ins>:

The default webdriver for this script is `Chrome`, which was the original web browser used in writing this script and executing the code.\
From a development perspective `Chrome` offers a better interface to inspect the HTML code needed in writing the scraper.

&nbsp;

However, other webdrivers, *e.g.* `Safari`, `Firefox`, and/or `Edge` may be used. 


To learn more about setting up the appropriate web driver, visit the Selenium web driver documentation [here](https://selenium-python.readthedocs.io/installation.html#drivers).


<p align="right"><a href="#top">(back to top)</a></p>

------

&nbsp;

## Quick Start

### <ins>Run in Terminal</ins> (*Recommended*):

In terminal run the following command: `python pop.py`, which will run the script with the default options (see below).


__<ins>Note</ins>:__ *If you have several versions of* `python`, *you will need to amend the above line to run your python3 alias, <strong>e.g.</strong> `python3 pop.py`.*


<p align="right"><a href="#top">(back to top)</a></p>

------

&nbsp;


## <ins>Advanced Options</ins>

There are a variety of optional arguments for the script, including timing, closet scroll size, closet ordering, the account to share, and the webdriver. 

To display the full range of command line arguments type `python3 pop.py --help` or `python3 pop.py -help`. 
For convenience, these options are described below.


### <ins>Timing</ins>:

You can adjust the timing from the command line. The default is 7200 seconds (*120 minutes* or *2 hours*). 

Using a shorter time period is *__not__ recommended* as it will be more likely caught by both captcha (`I am not a robot`) detection systems either at login or during the actual sharing. 

*Here are some examples:*
> - Every *four* hours: `python3 pop.py -t 14400`
> - Every *two* hours: `python3 pop.py -t 7200`


<p align="right"><a href="#top">(back to top)</a></p>

&nbsp;

### <ins>Closet Size</ins>:

The latest version of this code will automatically scroll to the end of your active listings in your closet. You should no longer need to adjust the number of possible scrolls (default, `n` = 1000). &nbsp;

If you desired to share only part of your closet, you could descrease the number of scrolls with the `-n` parameter: 


`python3 pop.py -n 1`


__<ins>Note</ins>:__ *The code above scrolls only 1 time.*


<p align="right"><a href="#top">(back to top)</a></p>

&nbsp;

### <ins>Closet Ordering</ins>:

To preserve closet order, the closet items must be shared in their reverse order. To this end, the default sorting is `order=True`:

__<ins>*Preserve Closet Order</ins>*:__
> 1. `python3 pop.py`
> 2. `python3 pop.py -o True`

To override this option, you can reverse order the items of the closet with the following flag, `-o False`:

* **Reverse Original Closet Order:** `python3 share.py -o False`


<p align="right"><a href="#top">(back to top)</a></p>

&nbsp;

### <ins>Account</ins>:

By default, the code will share all the listings for Poshmark account provided in `credentials.py`. 


While you will still need your account information in `credentials.py` to login, you may request that the code share the listings of another Depop user with the account option: `python3 pop.py -a another_depop_closet`.


Since the code is setup to run on a loop (by default every two hours), a safeguard is put in place to confirm that you actually want to share another user's account. 


This will appear in the terminal:
```
[*] you have requested to share
    the items in another Depop closet:
    ------------------------------------
    [*]: another_depop_closet
    ------------------------------------


[*] to confirm this request, enter [y]
    to cancel and share your closet items instead enter [n] :
y
```


__<ins>Note</ins>:__ *This prompt will occur each time the code runs.*


If you are confident you want to repeatedly share another users entire closet every few hours, you can bypass this prompt with the following command line option `b True`. 

<p align="right"><a href="#top">(back to top)</a></p>

&nbsp;

### <ins>Random Sharing Subset</ins>:

If you would prefer to not share your entire closet (or another account's entire closet), you may select to share a randomly selected subset of items from all possible active items. 


To do so, add the parameter `-r` followed by a number to your command in the terminal:\
`python3 pop.py -a another_depop_closet -r 25`

This shares 25 randomly selected items from another closet.

This functionality is helpful if you would like to share some of another person's closet, but not every item they have.

<p align="right"><a href="#top">(back to top)</a></p>

&nbsp;

### <ins>Webdriver</ins>:

Alternative `Selenium` web drivers may also be specified. Drivers may be called by entering their name, e.g. `-d Firefox` or `-d Chrome` or alternatively referring to the numerical shortcut for those options, e.g. `-d 0` or `-d 1`. 


The full list of *driver names and options* is as follows:
> - `Chrome` == 0
> - `Safari` == 1
> - `Firefox` == 2
> - `Edge` == 3


These must be properly installed on your system, otherwise you will encounter an error.

See [here](https://selenium-python.readthedocs.io/installation.html#drivers) for further details.


<p align="right"><a href="#top">(back to top)</a></p>
