const delay = 10;
async function swap(
  arr: any[],
  i: number,
  j: number,
  setchange: Function
): Promise<void> {
  const temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
  setchange(Math.random());
  await sleep(delay);
}
export async function sleep(delay: number) {
  await new Promise((r) => setTimeout(r, delay));
}

export async function bubbleSort(arr: any[], setchange: Function) {
  let i, j;
  for (i = 0; i < arr.length - 1; i++) {
    for (j = i; j < arr.length; j++) {
      if (arr[i].value > arr[j].value) {
        await swap(arr, i, j, setchange);
      }
    }
  }
}
