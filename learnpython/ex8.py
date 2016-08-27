def formatterN(n):
    formatter = ""
    for i in range(n):
        formatter += '%r'
        if i < n - 1:
            formatter += ' '
    return formatter

formatter4 = formatterN(4)

print formatter4 % (1, 2, 3, 4)
print formatter4 % ("one", "two", "three", "four")
print formatter4 % (True, False, False, True)
print formatter4 % (formatter4, formatter4, formatter4, formatter4)
print formatter4 % (
    "I had this thing.",
    "That you could type up right",
    "But it didn't sing.",
    "So I said goodnight",
)
