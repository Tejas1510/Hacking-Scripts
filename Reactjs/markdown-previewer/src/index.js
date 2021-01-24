import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import 'jquery/dist/jquery'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle'
const marked = require('marked');
const hljs = require('highlight.js');

const initialMarkdown = `
### Headers

# Header 1
## Header 2
###### Header 6

### List

- list item one
- list item two
- list item three

### Links

[Github](https://github.com)

[Youtube](https://www.youtube.com "youtube")

### Text Decorations

*italic*

**bold**

***bold and italic***

### Images

![Hacking Scripts](https://github.com/Tejas1510/Hacking-Scripts/raw/main/assets/Logos/logohackingscript.png 'Hacking Scripts')

### Blockquote

> To be, or not to be. That is a stupid question.

### Code

\`npm install create-react-app -g\`

\`\`\`
const number = Math.random() * 10
function sum(a, b) {
  return a + b
}
const name = 'Hacking Scripts'
\`\`\`
`

var renderer = new marked.Renderer()


renderer.link = function(href, title, text) {
  return `<a href=${href} target="_blank">${text}</a>`
}

marked.setOptions({
  renderer,
  highlight: function(code) {
    return hljs.highlightAuto(code).value
  },
  breaks: true
})

class App extends React.Component {
  constructor(props) {
    super(props)
    
    this.state = {
      markdown: initialMarkdown
    }
  }
  
  handleChange = e => this.setState({ markdown: e.target.value })
  
  render() {
    return (
      <div>
        <h1 style={{textAlign:'center', backgroundColor:'#61aeee', padding:'10px'}}>React Markdown Previewer</h1>
      <div className="container">
          <div className='left'>
            <textarea id='editor' value={this.state.markdown} onChange={this.handleChange}/>
          </div>
          <div className='right'>
            <div id='preview' dangerouslySetInnerHTML={{__html: marked(this.state.markdown)}} />
          </div>
      </div>
      </div>
    )
  }
}

ReactDOM.render(<App/>, document.getElementById('root'))