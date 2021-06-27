# EGGEGGEGG
data is stored using variables (eggs) which are referred to using numbers. the funny thing is that they are not infinite and the turtle lays a new egg every 5 commands. eggs can hold strings and signed integers.

commands are executed line by line and after each one delay between them is increased by 0.1 seconds (starting at 0) 

## values
these are used in **commands**

**value** - any type of value;
* if its a number then it returns a number
* if it starts with a " then it returns a string (if its at the end of the line then everything to the right split by spaces will be considered the same string), use \n for a newline and \s for a space
* if it starts with a $ then
  * if its followed by a number then it will return value of the egg with that number
  * if its followed by **c** it will return total value of eggs available
  * if its followed by **n** it will return the amount of eggs with nonzero values
  * if its followed by **z** it will return the amount of eggs with int 0's
* if its **i** it will return users input
* if its **n** it will return users input converted to int

**$egg** - $ followed by a number

## commands
comments start with \`

set **$egg value** - sets the value of **$egg** to **value**

is **value1 value2** - executes next line only if **value1** is equal to **value2** (those things work if next line is **is**, **isnot**, **while** or **whilenot**)

isnot **value1 value2** - executes next line only if **value1** is NOT equal to **value2**

while **value1 value2** - repeats next line while **value1** is equal to **value2**

whilenot **value1 value2** - repeats next line while **value1** is NOT equal to **value2**

out **value** - outputs **value**

turtle **value** - the turtle moves to line with number **value** (count from 0)

add **value1 value2 $egg** - adds **value1** to **value2** and saves into **$egg**

sub **value1 value2 $egg** - subtracts **value2** from **value1** and saves into **$egg**

mult **value1 value2 $egg** - multiplies **value1** by **value2** and saves into **$egg**

div **value1 value2 $egg** - divides **value1** by **value2** (integer division) and saves into **$egg**

conc **value1 value2 $egg** - concatenate **value1** and **value2** and save into **$egg**

toint **value $egg** - convert **value** to int if possible and save into **$egg**

tostr **value $egg** - convert **value** to str and save into **$egg**

free - you free the turtle (halt)

## examples
```
out "Hello, World!
```
this program outputs "Hello, World!"
```
whilenot $c 0
out i
```
this outputs whatever user inputs until total amount of eggs is 0, which is never so its an infinite loop

you can also do it like this
```
out i
turtle 0
```
