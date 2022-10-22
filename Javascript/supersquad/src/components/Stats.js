import React, { Component, Fragment } from 'react'
import { connect } from 'react-redux'
class Stats extends Component {
    calculatePower = (heros) => {
        let power = 0
        heros.forEach(item => power += item.power)
        return power
    }
    render() {
        const heros = this.props.heros
        return (
            <Fragment>
                <h4>Total Power: {this.calculatePower(heros)}</h4>
            </Fragment>
        )
    }
}

const mapStateToProps = state => {
    return {
        heros: state.Heros
    }
}

export default connect(mapStateToProps, null)(Stats)