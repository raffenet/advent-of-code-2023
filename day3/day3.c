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

static int check(char *p, size_t len);
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

    int part_sum = 0;
    for (char *p = input; *p != '\0'; p++) {
        if (*p == '\n') {
            continue;
        }

        if (isdigit(*p)) {
            size_t len = strspn(p, "0123456789");
            part_sum += check(p, len);
            p += len;
        }
    }

    /* sort by position of star */
    qsort(gears, num_gears, sizeof(struct gear), &compare);
    int sum = 0;
    char *skip = NULL;
    for (int i = 0; i < num_gears - 1; i++) {
        if (skip == gears[i].gear) {
            continue;
        }

        if ((gears[i].gear == gears[i+1].gear && i == num_gears - 2) ||
            (gears[i].gear == gears[i+1].gear && gears[i].gear != gears[i+2].gear)) {
            sum += gears[i].num * gears[i+1].num;
        } else if (gears[i].gear == gears[i+1].gear && gears[i].gear == gears[i+2].gear) {
            skip = gears[i].gear;
        }
    }

    free(input);
    free(gears);

    printf("parts = %d\n", part_sum);
    printf("ratio = %d\n", sum);

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

static inline int isgear(char c)
{
    return c == '*';
}

static inline int issymbol(char c)
{
    return (!isdigit(c) && c != '.');
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
    if (!IS_TOP(p - input) && issymbol(*(p + UP))) {
        if (isgear(*(p + UP))) {
            append_gear(p + UP, num);
        }
        return 1;
    }

    return 0;
}

static int down(char *p, int num)
{
    if (!IS_BOTTOM(p - input) && issymbol(*(p + DOWN))) {
        if (isgear(*(p + DOWN))) {
            append_gear(p + DOWN, num);
        }
        return 1;
    }

    return 0;
}

static int left(char *p, int num) {
    int ret = 0;
    if (!LEFT_EDGE(p - input)) {
        p--;
        if (issymbol(*p)) {
            if (isgear(*p)) {
                append_gear(p, num);
            }
            ret |= 1;
        }
        ret |= up(p, num);
        ret |= down(p, num);
    }

    return ret;
}

static int right(char *p, int num) {
    int ret = 0;
    if (!RIGHT_EDGE(p - input)) {
        p++;
        if (issymbol(*p)) {
            if (isgear(*p)) {
                append_gear(p, num);
            }
            ret |= 1;
        }
        ret |= up(p, num);
        ret |= down(p, num);
    }

    return ret;
}

static int check(char *p, size_t size)
{
    int is_part = 0;
    char *num = malloc(size + 1);
    strncpy(num, p, size);
    num[size] = '\0';
    int part_num = atoi(num);
    free(num);

    for (int i = 0; i < size; i++,p++) {
        if (i == 0) {
            is_part |= left(p, part_num);
        }
        is_part |= up(p, part_num);
        is_part |= down(p, part_num);
        if (i == size - 1) {
            is_part |= right(p, part_num);
        }
    }

    return is_part ? part_num : 0;
}

static int compare(const void *arg1, const void *arg2)
{
    return ((const struct gear *)arg1)->gear - ((const struct gear *)arg2)->gear;
}
