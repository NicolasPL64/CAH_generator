# Cards Against Humanity card generator

This program generates a ready-to-print PDF with cards for the game [Cards Against Humanity](https://cardsagainsthumanity.com/) given plain text files (.txt).

## New features and improvements from the original branch

- 3 different variations (examples down below)
- Support for special characters
- Support for HTML tags (like \<i> or \<br/>)
- Improved the line-splitting method
- Lots of bugs fixed!

## Usage

File(s) with sentences must be placed inside **Input/BlackCards** and **Input/WhiteCards** respectively (one line = one card). Multiple files can be placed in their respective folders, thus allowing for more organization.

Install program dependencies:

```bash
$ pip3 install -r requirements.txt 
```

Choose between any of the three variations, run the corresponding script and see the result in **Output/**:

```bash
$ ./[3] centered 4x5.py
```

## Example
Given the files *Input/BlackCards/A testing.txt*, *Input/BlackCards/black.txt*, *Input/WhiteCards/A testing.txt* and *Input/WhiteCards/white.txt* the output folder will contain a PDF like this:

*Variation 1:*
![1](https://github.com/NicolasPL64/CAH_generator/assets/31411531/cb2c0606-536e-4b8b-a932-cb1d581ef07d)

*Variation 2:*
![2](https://github.com/NicolasPL64/CAH_generator/assets/31411531/a09bff81-bacf-4e05-ae3d-303c14aaaa30)

*Variation 3:*
![3](https://github.com/NicolasPL64/CAH_generator/assets/31411531/e515e74e-6866-4cb2-9738-aed086683734)


## Why?
I didn't want to waste 10 minutes writing cards into a PDF then I thought that it would be a great idea to waste one day writing a program to make it automatically. - @Rubenmp

And I wanted to fix the original code to satisfy my needs as I'll be using this script in the future to print some evil cards to play with my friends! (Also I wanted to learn python, this was my first time lol) - @NicolasPL64

## License
Creative Commons BY-NC-SA 2.0
