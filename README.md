This is a project I completed using Python as part of my freeCodeCamp course.

I created a function in Python to arrange arithmetic problems vertically. This received a list of strings that are arithmetic problems and returned the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

For example, if I call the function with the following list of problems:

```
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
```

The function should return the following output:

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
   40     3799     88    172
```

If I call the function with the following list of problems and set the second argument to True:

```
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True
```

The function should return the following output:

```
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

The function will return the correct conversion if the supplied problems are properly formatted. Otherwise, it will return a string that describes an error that is meaningful to the user.

Here are the situations that will return an error:

* If there are more than five problems supplied to the function.
* If the operator is not `+` or `-`.
* If either number (operand) contains any characters other than digits.
* If either operand is more than four digits long.

If the user supplies the correct format of problems, the conversion I will return will follow these rules:

* There should be a single space between the operator and the longest of the two operands.
* The operator will be on the same line as the second operand.
* Both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
* Numbers should be right-aligned.
* There should be four spaces between each problem.
* There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.

I wrote to write my code in `arithmetic_arranger.py`. For development, I can use `main.py` to test my `arithmetic_arranger()` function. 

The unit tests for this project were in  `test_module.py `. We were running the tests from `test_module.py ` in main.py for my convenience. The tests would run automatically whenever I hit the "run" button. Alternatively, I could run the tests by inputting pytest in the console.
