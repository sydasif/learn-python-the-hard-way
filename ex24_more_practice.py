print("Let's practice everything.")
print('You\'d need to know \'about escapes with \\ that do:')
print('\nnewlines and \ttabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("-----------------")
print(poem)
print("------------------")


five = 10 - 2 + 3 -6
print(f"This should be five {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# its just like with an f"" string
print(f"We'd have Beans: {beans}, Jars: {jars} and Crates: {crates}")

start_point = start_point / 10

formula = secret_formula(start_point)
print("We can also do that this way")
# this is an easy way to apply a list to a format string
print("Beans: {}, Jars: {}, Crates: {}".format(*formula))
