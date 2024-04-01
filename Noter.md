### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### The Augmented Assignment Operators

| Augmented assignment statementcol | Equivalent assignment statement |
| --------------------------------- | :------------------------------ |
| spam = spam + 1                   | spam += 1                       |
| spam = spam - 1                   | spam -= 1                       |
| spam = spam * 1                   | spam *= 1                       |
| spam = spam / 1                   | spam /= 1                       |
| spam = spam % 1                   | spam %= 1                       |

Escoae Characters

| Escape character | Print as             |
| ---------------- | :------------------- |
| \\'              | single qutoe         |
| \\"              | Double qutoes        |
| \t               | tab                  |
| \n               | Newline (Line break) |
| \\\              | Backslash            |

####

String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

| Escape character | Print as                 |
| ---------------- | ------------------------ |
| '                | Single quote             |
| !=               | Not equal to             |
| <                | Less than                |
| >                | Greater than             |
| <=               | Less than or equal to    |
| >=               | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator opera∏tes on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

#### Math Operators from Highest to Lowest Precedence

| Operator | Operation                         | Example | Evaluates to... |
| -------- | --------------------------------- | ------- | --------------- |
| **       | Exponent                          | 2 ** 3  | 8               |
| %        | Modulus/remainder                 | 22 % 8  | 6               |
| //       | Integer division/floored quotient | 22 // 8 | 2               |
| /        | Division                          | 22 / 8  | 2.75            |
| *        | Multiplication                    | 3 * 5   | 15              |
| -        | Subtraction                       | 5- 2    | 3               |
| +        | Addition                          | 2+ 2    | 4               |

#### Common Data Types

| Data type              | Examples                                |
| ---------------------- | --------------------------------------- |
| Integers               | -2, -1, 0, 1, 2, 3, 4, 5                |
| Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| Strings                | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |

#### Comparison operators

Comparison operators compare two values and evaluate down to a single Boolean value.

| Operator | Meaning                  |
| -------- | ------------------------ |
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

#### String concatenation and replication

```
>>> 'Alice' + 'Bob' 
'AliceBob'
```

```
>>> 'Alice' * 5 
'AliceAliceAliceAliceAlice'
```

## Common functions

**The print() function**

The print() function displays the string value inside the parentheses on the screen.

```
print('Hello world!')
print('What is your name?') # ask for their name
```

**The input() function**

The input() function waits for the user to type some text on the keyboard and press enter.

```
myName = input()
```

**The len() function**

You can pass the len() function a string value (or a variable containing a string), and the function evaluates to the integer value of the number of characters in that string.

```
>>> len('hello')
5
>>> len('My very energetic monster just scarfed nachos.') 
46
>>> len('')
0
```

## Binary Boolean Operators

A truth table shows every possible result of a Boolean operator. Table 2-2
is the truth table for the and operator.

| Expression      | Evaluates to... |
| --------------- | --------------- |
| True and True   | True            |
| True and False  | False           |
| False and True  | False           |
| False and False | False           |

### The not Operator

Unlike and and or, the not operator operates on only one Boolean value (or
expression). The not operator simply evaluates to the opposite Boolean value.

| Expression | Evaluates to... |
| ---------- | --------------- |
| not True   | False           |
| not False  | True            |

## Def Statements with Parameters

When you call the len() function and pass it an argument such as 'Hello',
the function call evaluates to the integer value 5, which is the length of the
string you passed it. In general, the value that a function call evaluates to is
called the return value of the function.
When creating a function using the def statement, you can specify what
the return value should be with a return statement. A return statement con-
sists of the following:

- The*return* keyword
- The value or expression that the function should return

When an expression is used with a return statement, the return value
is what this expression evaluates to. For example, the following program
defines a function that returns a different string depending on what num-
ber it is passed as an argument.

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

```
import random

def getAnswer(answerNumber):
	if answerNumber == 1:
		return "It is certain"
	elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9) 
fortune = getAnswer(r) 
print(fortune)

```

## List

**Using for Loops with Lists**

```
>>> supplies = ['pens', 'staplers', 'flame-throwers', 'binders'] >>> for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
```

Using range(len(supplies)) in the previously shown for loop is handy
because the code in the loop can access the index (as the variable i) and
the value at that index (as supplies[i]). Best of all, range(len(supplies)) will
iterate through all the indexes of supplies, no matter how many items it
contains.

#### Sorting the Values in a List with the sort() Method

Lists of number values or lists of strings can be sorted with the sort()
method. For example, enter the following into the interactive shell:

```
>>> spam = [2, 5, 3.14, 1, -7] >>> spam.sort()
>>> spam
[-7, 1, 2, 3.14, 5]
>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants'] >>> spam.sort()
>>> spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

## Dictionaries

#### The keys(), values(), and items() Methods

There are three dictionary methods that will return list-like values of thedictionary’s keys, values, or both keys and values: keys(), values(), and items().The values returned by these methods are not true lists: They cannot be modified and do not have an append() method. But these data types (dict_keys dict_values, and dict_items, respectively) can be used in for loops.

```
>>> spam = {'color': 'red', 'age': 42} >>> for v in spam.values():
print(v)
red 42
```

#### The get Method

It’s tedious to check whether a key exists in a dictionary before accessing
that key’s value. Fortunately, dictionaries have a get() method that takes two
arguments: the key of the value to retrieve and a fallback value to return if
that key does not exist.

```
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' 'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' 'I am bringing 0 eggs.'
```

### The setdefault() Method

You’ll often have to set a value in a dictionary for a certain key only if that key does not already have a value. The code looks something like this:

```
 spam = {'name': 'Pooka', 'age': 5}
                 if 'color' not in spam:
                     spam['color'] = 'black'
```
