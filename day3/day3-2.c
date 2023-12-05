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

static void check(char *p, size_t len);
static int compare(const void *arg1, const void *arg2);

struct gear {
    int num;
    char *gear;
};
static struct gear *gears;
static int num_gears;
static int capacity = 1024;

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

    gears = malloc(sizeof(struct gear) * capacity);
    num_gears = 0;

    for (char *p = input; *p != '\0'; p++) {
        if (*p == '\n') {
            continue;
        }

        if (isdigit(*p)) {
            size_t len = strspn(p, "0123456789");
            check(p, len);
            p += len;
        }
    }

    /* sort by position of star */
    qsort(gears, capacity, sizeof(struct gear), &compare);
    int i;
    int sum = 0;
    char *skip = NULL;
    for (i = 0; i < capacity - 1; i++) {
        if (skip == gears[i].gear) {
            continue;
        }
        if (gears[i].gear == gears[i+1].gear && i == capacity - 2) {
            sum += gears[i].num * gears[i+1].num;
        } else if (gears[i].gear == gears[i+1].gear && gears[i].gear != gears[i+2].gear) {
            sum += gears[i].num * gears[i+1].num;
        } else if (gears[i].gear == gears[i+1].gear && gears[i].gear == gears[i+2].gear) {
            skip = gears[i].gear;
        }
    }

    free(input);
    free(gears);

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

static int isgear(char c)
{
    return c == '*';
}

static void append_gear(char *p, int num)
{
    gears[num_gears].gear = p;
    gears[num_gears].num = num;
    num_gears++;
    if (num_gears == capacity) {
        capacity *= 2;
        gears = realloc(gears, capacity * sizeof(struct gear));
    }
}

static int up(char *p, int num)
{
    if (!IS_TOP(p - input) && isgear(*(p + UP))) {
        append_gear(p + UP, num);
    }

    return 0;
}

static int down(char *p, int num)
{
    if (!IS_BOTTOM(p - input) && isgear(*(p + DOWN))) {
        append_gear(p + DOWN, num);
    }

    return 0;
}

static int left(char *p, int num) {
    if (!LEFT_EDGE(p - input)) {
        p--;
        if (isgear(*p)) {
            append_gear(p, num);
        }
        up(p, num);
        down(p, num);
    }

    return 0;
}

static int right(char *p, int num) {
    if (!RIGHT_EDGE(p - input)) {
        p++;
        if (isgear(*p)) {
            append_gear(p, num);
        }
        up(p, num);
        down(p, num);
    }

    return 0;
}

static void check(char *p, size_t size)
{
    char *num = malloc(size + 1);
    strncpy(num, p, size);
    num[size] = '\0';
    int part_num = atoi(num);
    free(num);

    for (int i = 0; i < size; i++,p++) {
        if (i == 0) {
            left(p, part_num);
        }
        up(p, part_num);
        down(p, part_num);
        if (i == size - 1) {
            right(p, part_num);
        }
    }
}

static int compare(const void *arg1, const void *arg2)
{
    return ((const struct gear *)arg1)->gear - ((const struct gear *)arg2)->gear;
}
