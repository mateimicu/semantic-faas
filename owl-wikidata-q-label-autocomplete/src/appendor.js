const append = (text, owlStatements) => {
  owlStatements.forEach(owlStatement => {
    text += `\n${ owlStatement }`;
  });

  console.log(text);
  return text;
}

export default { append };