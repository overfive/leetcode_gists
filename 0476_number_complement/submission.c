int findComplement(int num) {
    return (1 - num % 2) + 2 * (num <= 1 ? 0 : findComplement(num >> 1));
}
