
#ifndef _ALLOCATE_H_
#define _ALLOCATE_H_


#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdarg.h>
#include "typeutil.h"

void *get_spc(int32_t num, size_t size);
void *mget_spc(int32_t num, size_t size);
void **get_img(int32_t wd, int32_t ht, size_t size);
void free_img(void **pt);
void *multialloc(size_t s, int32_t d, ...);
void multifree(void *r,int32_t d);

#endif /* _ALLOCATE_H_ */

