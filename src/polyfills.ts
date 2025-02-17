// Polyfill for Array.at
const typedArray = Reflect.getPrototypeOf(Int8Array);
for (const c of [Array, String, typedArray]) {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  Object.defineProperty(c.prototype, "at",
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    { value: function at(n: any) {
      // ToInteger() abstract op
      n = Math.trunc(n) || 0;
      // Allow negative indexing from the end
      if (n < 0) n += this.length;
      // OOB access is guaranteed to return undefined
      if (n < 0 || n >= this.length) return undefined;
      // Otherwise, this is just normal property access
      return this[n];
    },
    writable: true,
    enumerable: false,
    configurable: true });
}
