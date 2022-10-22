import React, { Component } from 'react'
import { connect } from 'react-redux'
import { removeCharacterById } from '../actions/index'
class HerosList extends Component {
    render() {
        let heros = this.props.heros
        console.log("Heros props ", this.props)
        return (
            <div>
                <h4>Heros List</h4>
                <ul>
                    {
                        heros.map(hero => {
                            return (
                                <li key={hero.id}>
                                    <div style={{ display: 'inline' }}>{hero.name}&nbsp; &nbsp;</div>
                                    <div style={{ display: 'inline', cursor: 'pointer' }} onClick={() => this.props.removeCharacterById(hero.id)}>-</div>
                                </li>
                            )
                        })
                    }
                </ul>
            </div>
        )
    }
}

const mapStateToprops = state => {
    console.log('from heros', state.Heros)
    return {
        heros: state.Heros
    }
}
export default connect(mapStateToprops, { removeCharacterById })(HerosList)