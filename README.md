# Cards Against Humanity card generator

This program generates a PDF with cards for the game [Cards Against Humanity](https://cardsagainsthumanity.com/) given several plain text files.


## Usage

File(s) with sentences must be placed inside **Input/BlackCards** and **Input/WhiteCards** respectively (one sentence per line). Multiple files can be placed in their respective folders thus allowing for more organization.

Install program dependencies

```bash
$ pip3 install -r requirements.txt 
```

Run the program and see the result in **Output/**

```bash
$ ./main.py
```

## Example
Given these files *Input/BlackCards/example.txt* and *Output/WhiteCards/example.txt* the output file will contain:

![Cards](./cards.png)

## Why?
I didn't want to waste 10 minutes writing cards into a PDF, so I thought that it would be a great idea to waste one day writing a program to make it automatically.

## License
Creative Commons BY-NC-SA 2.0
