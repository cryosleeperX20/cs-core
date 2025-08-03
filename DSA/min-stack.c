/*Design a stack that supports:
push(x)
pop()
top()
getMin() — returns the minimum element in the stack, all in O(1) time.
*/

typedef struct {
    int *stack;
    int *minStack;
    int top;
    int size;
} MinStack;

MinStack* minStackCreate() {
    MinStack* obj = malloc(sizeof(MinStack));
    obj->size = 10000;
    obj->stack = malloc(sizeof(int) * obj->size);
    obj->minStack = malloc(sizeof(int) * obj->size);
    obj->top = -1;
    return obj;
}

void minStackPush(MinStack* obj, int val) {
    obj->stack[++obj->top] = val;
    if (obj->top == 0) {
        obj->minStack[obj->top] = val;
    } else {
        int currentMin = obj->minStack[obj->top - 1];
        obj->minStack[obj->top] = val < currentMin ? val : currentMin;
    }
}

void minStackPop(MinStack* obj) {
    if (obj->top >= 0) {
        obj->top--;
    }
}

int minStackTop(MinStack* obj) {
    return obj->stack[obj->top];
}

int minStackGetMin(MinStack* obj) {
    return obj->minStack[obj->top];
}

void minStackFree(MinStack* obj) {
    free(obj->stack);
    free(obj->minStack);
    free(obj);
}
