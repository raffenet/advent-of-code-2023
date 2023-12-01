#include <string.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

static int aoc_isdigit(const char *str, char *digit);

int main(void)
{
    int sum = 0;

    FILE *fd = fopen("input.txt", "r");
    fseek(fd, 0, SEEK_END);
    long size = ftell(fd);
    rewind(fd);

    char *input = malloc(size + 1);
    fread(input, 1, size, fd);
    input[size - 1] = '\0';
    fclose(fd);

    char *tofree = input;
    char *token;
    while ((token = strsep(&input, "\n")) != NULL) {
        char calibration[3] = "xx";

        /* search for first and last digit */
        for (int i = 0; i < strlen(token); i++) {
            char digit;
            if (aoc_isdigit(&token[i], &digit)) {
                if (calibration[0] == 'x') {
                    calibration[0] = digit;
                    calibration[1] = digit;
                } else {
                    calibration[1] = digit;
                }
            }
        }

        sum += atoi(calibration);
    }
    free(tofree);

    printf("sum = %d\n", sum);
    return 0;
}

/*** utils ***/

static inline int aoc_strcmp(const char *a, const char *b)
{
    return strncmp(a, b, strlen(b));
}

static int aoc_isdigit(const char *str, char *digit)
{
    if (isdigit(str[0])) {
        *digit = str[0];
        return 1;
    } else if (aoc_strcmp(str, "one") == 0) {
        *digit = '1';
        return 1;
    } else if (aoc_strcmp(str, "two") == 0) {
        *digit = '2';
        return 1;
    } else if (aoc_strcmp(str, "three") == 0) {
        *digit = '3';
        return 1;
    } else if (aoc_strcmp(str, "four") == 0) {
        *digit = '4';
        return 1;
    } else if (aoc_strcmp(str, "five") == 0) {
        *digit = '5';
        return 1;
    } else if (aoc_strcmp(str, "six") == 0) {
        *digit = '6';
        return 1;
    } else if (aoc_strcmp(str, "seven") == 0) {
        *digit = '7';
        return 1;
    } else if (aoc_strcmp(str, "eight") == 0) {
        *digit = '8';
        return 1;
    } else if (aoc_strcmp(str, "nine") == 0) {
        *digit = '9';
        return 1;
    }

    return 0;
}
