const fs = require('fs');

//const testFilePath = '../../docs/references/terms_definitions.md';

const filePath = process.argv.slice(2).pop();

if(!filePath){
  const path = require('path');
  const appPath=process.argv.slice(0, 2).map(s=>path.basename(s)).join(' ')
  console.error(`Usage: ${appPath} <inputFile>`)
  throw process.exit(1);
}

const source = fs.readFileSync(filePath).toString();

const reIsSectionTitle = /^##\s+(.+)$/i;
const reSkipLine = /^(\r|\n|\r\n|\n\r)$/;

const getPageSections =(source)=>{
  const lines = source.split(/(\r\n|\n\r|\n|\r)/g);

  return lines.reduce((sections, line)=>{
    if(reIsSectionTitle.exec(line)){
      const newSectionTitle = reIsSectionTitle.exec(line)[1];
      return [...sections, {name: newSectionTitle, contents: ''}];
    }
    if(reSkipLine.exec(line)){
      return sections;
    }
    const section = sections.pop();
    return [...sections, {...section, contents: `${section.contents}${line}\n`}];
  }, [{contents:''}]).sort(({name: nameA}, {name: nameB})=>{
    if(!nameA){
      return -1;
    }
    if(!nameB){
      return 1;
    }
    return nameA.localeCompare(nameB);
  });
}

const sections = getPageSections(source);

console.log(sections.reduce((doc, {name = '', contents = ''})=>{
  if(name){
    return `${doc}## ${name}\n${contents}`;
  }
  return `${doc}${contents}`;
}, '').trim());
