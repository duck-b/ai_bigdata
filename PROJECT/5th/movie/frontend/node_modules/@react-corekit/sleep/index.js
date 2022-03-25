module.exports = n => {
  return new Promise(resolve => setTimeout(resolve, n));
};
