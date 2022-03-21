# reg ex greedy/non greedy, repetitions
# lesson 26
# pages 
# reg ex groups and pipe character
# 


# summmary
# ? = says group matches zero or one times
# * = zero or more times
# + = one or more times
# { } = match specific number of times
# { } w/ some number matches minimum and max number of times
# leaving out first or seond number in curly braces says there is no min or max
# "greedy" matching will match logest string possible
# "nongreed" matching will match shortest string possible
# putting ? after curly braces makes it do a nongreedy match


# phoneRegex2 = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

#digitRegex = re.compile(r'(\d){3,5}?') # with ? added output is 123
#digi = digitRegex.search('1234567890')

#print(digi.group()) # ouptput is 12345 w/out ? in regex pattern, with ? it just goes to 3 as in 123
#print(digi) # output is that it's a match

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#digi = digitRegex.search('1234567890')

###################################################### find all

LongSringExample = '''
chia-plotter (pipelined multi-threaded)
This is a new implementation of a chia plotter which is designed as a processing pipeline, similar to how GPUs work, only the "cores" are normal software CPU threads.

As a result this plotter is able to fully max out any storage device's bandwidth, simply by increasing the number of "cores", ie. threads.

Sponsored by Flexpool.io - Check them out if you're looking for a secure and scalable Chia pool.

Usage
Join the Discord for support: https://discord.gg/pQwkebKnPB

For <poolkey> and <farmerkey> see output of `chia keys show`.
To plot for pools, specify <contract> address via -c instead of <poolkey>, see `chia plotnft show`.
<tmpdir> needs about 220 GiB space, it will handle about 25% of all writes. (Examples: './', '/mnt/tmp/')
<tmpdir2> needs about 110 GiB space and ideally is a RAM drive, it will handle about 75% of all writes.
Combined (tmpdir + tmpdir2) peak disk usage is less than 256 GiB.
In case of <count> != 1, you may press Ctrl-C for graceful termination after current plot is finished,
or double press Ctrl-C to terminate immediately.

555-223-3342

Usage:
  chia_plot [OPTION...]

  -k, --size arg       K size (default = 32, k <= 32)
  -x, --port arg       Network port (default = 8444, chives = 9699)
  -n, --count arg      Number of plots to create (default = 1, -1 = infinite)
  -r, --threads arg    Number of threads (default = 4)
  -u, --buckets arg    Number of buckets (default = 256)
  -v, --buckets3 arg   Number of buckets for phase 3+4 (default = buckets)
  -t, --tmpdir arg     Temporary directory, needs ~220 GiB (default = $PWD)
  -2, --tmpdir2 arg    Temporary directory 2, needs ~110 GiB [RAM] (default = <tmpdir>)
  -d, --finaldir arg   Final directory (default = <tmpdir>)
  -w, --waitforcopy    Wait for copy to start next plot
  -p, --poolkey arg    Pool Public Key (48 bytes)
  -c, --contract arg   Pool Contract Address (62 chars)
  -f, --farmerkey arg  Farmer Public Key (48 bytes)
  -G, --tmptoggle      Alternate tmpdir/tmpdir2 (default = false)
  -D, --directout      Create plot directly in finaldir (default = false)
  -K, --rmulti2 arg    Thread multiplier for P2 (default = 1)
      --help           Print help
Make sure to crank up <threads> if you have plenty of cores, the default is 4. Depending on the phase more threads will be launched, the setting is just a multiplier.

RAM usage depends on <threads> and <buckets>. With the new default of 256 buckets it's about 0.5 GB per thread at most.

-G option will alternate the temp dirs used while plotting to give each one, tmpdir and tmpdir2, equal usage. The first plot creation will use tmpdir and tmpdir2 as expected. The next run, if -n equals 2 or more, will swap the order to tmpdir2 and tmpdir. The next run swaps again to tmpdir and tmpdir2. This will occur until the number of plots created is reached or until stopped.

RAM disk setup on Linux
sudo mount -t tmpfs -o size=110G tmpfs /mnt/ram/

Note: 128 GiB System RAM minimum required for RAM disk.

111-555-1234

How to Support
XCH: xch1w5c2vv5ak08pczeph7tp5xmkl5762pdf3pyjkg9z4ks4ed55j3psgay0zh

XFX: xfx1succfn2z3uwmq50ukztjanrvs9kw294mqn4lv22rk6tzmcu7e2xsyxyaa5

XCC: xcc16j65y35fs8u289nq6krcyehsmp5eqd4we493rxf36pg7eymcqrqqltsrat

ETH-ERC20: 0x97057cdf529867838d2a1f7f23ba62456764e0cd

LTC: MNUnszsX2srv5EJpu9YYHAXb19MqUpuBjD

BTC: 15GSE5ymStxXMvJ58hyosEVm4FXFxUyJZg

Results
On a dual Xeon® E5-2650v2@2.60GHz R720 with 256GB RAM and a 3x800GB SATA SSD RAID0, using a 110G tmpfs for <tmpdir2>:

Click to expand
How to Verify
To make sure the plots are valid you can use the ProofOfSpace tool from chiapos:

git clone https://github.com/Chia-Network/chiapos.git
cd chiapos && mkdir build && cd build && cmake .. && make -j8
./ProofOfSpace check -f plot-k32-???.plot [num_iterations]
How to update to latest version
cd chia-plotter
git checkout master
git pull
git submodule update --init
./make_devel.sh
Future Plans
I do have some history with GPU mining, back in 2014 I was the first to open source a XPM GPU miner, which was about 40x more efficient than the CPU miner. See my other repos.

As such, it's only a matter of time until I add OpenCL support to speed up the plotter even more, keeping most of the load off the CPUs.

999-000-8877

Dependencies
cmake (>=3.14)
libsodium-dev
Install
 '''
sResult = phoneRegex.search(LongSringExample)
#phoneRegex.findall()

#print('just using the search method - ' + sResult.group()) # only the first phone number found is displayed

sFindAllMatches  = phoneRegex.findall(LongSringExample)
#print('with the find all method - ' + str(sFindAllMatches))

# notes:
# search returns match objects
# findall returns list of strings

# behavrior for regex objects that have or one groups in them (groups being with the \d\d\d inside () ) is 
# find all returns list of strings will just be text foundmatching that pattern
# see lesson 26 around 3 minutes in for phrasing with on-screen "correction"


phoneRegex2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
sfindallMatchesEx2 = phoneRegex2.findall(LongSringExample)
# returns have strings, tuples
# has zero or one groups == list of strings
# if has two or more groups list of tuples of strings

# below doesn't have any .group() method because it's a list of strings, not an object
#print(sfindallMatchesEx2) # returns all the numbers from that giant sample text block I put in succesfully
# output
# [('555-223-3342', '555', '223-3342'), ('111-555-1234', '111', '555-1234'), ('999-000-8877', '999', '000-8877')]

# character classses

#digitRegex = re.compile('(0|1|2|3|4|5|6|7|8|9') # same is /d
# table 7-1 in the book
# /D (cap D) is "any character not numberic between 0 and 9"
# /w is "any letter, numberic digit or underscore character" referred to as "word"
# /W (cap W) "any character that is NOT a letter, numberic digit or underscore character" 
# /s any space, tab or newline character (e.g. "matching the space characters")
# /S (cap S) any character NOT space, tab or newline character (e.g. "matching the space characters")

# 12 days of xmas example

sTwelveDayXmasLyrics = ''' 
On the first day of Christmas
My true love sent to me
A partridge in a pear tree
On the second day of Christmas
My true love sent to me
2 turtle-doves
And a partridge in a pear tree
On the third day of Christmas
My true love sent to me
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 4th day of Christmas
My true love sent to me
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the fifth day of Christmas
My true love sent to me
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 6th day of Christmas
My true love sent to me
6 geese a laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 7th day of Christmas
My true love sent to me
7 swans a swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 8h day of Christmas
My true love sent to me
8 maids a milking
7 swans a swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the ninth day of Christmas
My true love sent to me
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 10th day of Christmas
My true love sent to me
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 11th day of Christmas
My true love sent to me
I sent 11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
On the 12th day of Christmas
My true love sent to me
12 drummers drumming
11 pipers piping
10 lords a-leaping
9 ladies dancing
8 maids a-milking
7 swans a-swimming
6 geese a-laying
4 golden rings (4 golden rings)
4 calling birds
3 French hens
2 turtle-doves
And a partridge in a pear tree
And a partridge in a pear tree
'''

xmasRegex = re.compile(r'\d+\s\w+')

xmasResults = xmasRegex.findall(sTwelveDayXmasLyrics)
#print(xmasResults)

vowelRegex = re.compile('[aeiouAEIOU]')
#vResult = vowelRegex.findall(sTwelveDayXmasLyrics)
#print(vResult)

#DoubleVowelRegex = re.compile('[aeiouAEIOU]{2}')
#vResult = DoubleVowelRegex.findall(sTwelveDayXmasLyrics) # matches two vowels at a time
#print(vResult)

# negative character classes 
# using carrots
NegVowelRegex = re.compile(r'[^aeiouAEIOU]{2}') # opposite e.g. "find the opposite" for all non-vowels
vResult = NegVowelRegex.findall(sTwelveDayXmasLyrics) # matches two vowels at a time
print(vResult)

# make cusotm/own character classes with [] e.g [aeiou]
# a caret ^ makes a negative character class, matching anything NOT in the backets, like [^aeiou] for all non-vowels

