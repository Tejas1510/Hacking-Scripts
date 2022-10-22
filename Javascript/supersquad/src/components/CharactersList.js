import React, { Component } from 'react'
import { connect } from 'react-redux'
import { bindActionCreators } from 'redux'
import { addCharacterById } from '../actions/index'

class CharactersList extends Component {
    render() {
        console.log("FROM PROPS", this.props)
        const { characters } = this.props
        return (

            <div>
                <h3>Characters list</h3>
                <ul>
                    {/* {characters.map(item => return (<li key={item.id}>{item.name}</li>))} */}
                    {characters.map(character => {
                        return (
                            <li key={character.id} >
                                <div style={{ display: 'inline' }}>{character.name}  &nbsp; &nbsp;</div>
                                <div style={{ display: 'inline', cursor: 'pointer' }} onClick={() => this.props.addCharacterById(character.id)}>+</div>
                            </li>
                        )
                    })
                    }

                </ul>

            </div>
        )
    }
}

const mapStateToProps = state => {
    // console.log('From map state to props ', state) -> current store
    return {
        characters: state.Characters
    }
}

// const mapDispatchToProps = dispatch => {
//     return bindActionCreators({ addCharacterById }, dispatch)
// }
export default connect(mapStateToProps, { addCharacterById })(CharactersList)