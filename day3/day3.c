#include <string.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

#define PROD

#ifdef PROD
#define INPUT "input.txt"
#else
#define INPUT "sample.txt"
#endif

char *input;

static int check(char *position, size_t len);

int main(void)
{
    FILE *fd = fopen(INPUT, "r");
    fseek(fd, 0, SEEK_END);
    long size = ftell(fd);
    rewind(fd);

    input = malloc(size + 1);
    fread(input, 1, size, fd);
    input[size - 1] = '\0';
    fclose(fd);

    int sum = 0;
    for (char *p = input; *p != '\0'; p++) {
        if (*p == '\n') {
            continue;
        }

        if (isdigit(*p)) {
            size_t len = strspn(p, "0123456789");
            /* do checking */
            sum += check(p, len);
            p += len;
        }
    }

    free(input);

    printf("sum = %d\n", sum);

    return 0;
}

/*** utils ***/

#ifdef PROD
#define UP         (-141)
#define DOWN       (141)
#define LEFT_EDGE(x) ((x) % 141 == 0)
#define RIGHT_EDGE(x) (((x) - 139) % 141 == 0)
#define IS_TOP(x) ((x) < 140)
#define IS_BOTTOM(x) ((x) > 141*139 - 1)
#else
#define UP         (-11)
#define DOWN       (11)
#define LEFT_EDGE(x) ((x) % 11 == 0)
#define RIGHT_EDGE(x) (((x) - 9) % 11 == 0)
#define IS_TOP(x) ((x) < 10)
#define IS_BOTTOM(x) ((x) > 98)
#endif

static int issymbol(char c)
{
    return !isdigit(c) && c != '.';
}

static int up(char *p)
{
    if (!IS_TOP(p - input)) {
        return issymbol(*(p + UP));
    }

    return 0;
}

static int down(char *p)
{
    if (!IS_BOTTOM(p - input)) {
        return issymbol(*(p + DOWN));
    }

    return 0;
}

static int back(char *p) {
    if (!LEFT_EDGE(p - input)) {
        p--;
        return (issymbol(*p) || up(p) || down(p));
    }

    return 0;
}

static int forward(char *p) {
    if (!RIGHT_EDGE(p - input)) {
        p++;
        return (issymbol(*p) || up(p) || down(p));
    }

    return 0;
}

static int check(char *p, size_t size)
{
    char *num = malloc(size + 1);
    strncpy(num, p, size);
    num[size] = '\0';
    int part_num = atoi(num);
    free(num);

    int is_part;
    for (int i = 0; i < size; i++,p++) {
        is_part = up(p) || down(p) || back(p) || forward(p);
        if (is_part) {
            return part_num;
        }
    }

    return 0;
}
