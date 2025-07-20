```c
#include <stdio.h>
#include <string.h>

// Vulnerable binary for Stack Smash challenge
// Uses gets() with a fixed-size buffer, no stack protections

int main() {
    char buffer[64];
    printf("Enter your input: ");
    gets(buffer); // Vulnerable to buffer overflow
    printf("You entered: %s\n", buffer);
    return 0;
}
```
