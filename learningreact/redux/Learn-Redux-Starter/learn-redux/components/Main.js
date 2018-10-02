import react from 'react';
import { Link } from 'react-router';
import { disconnect } from 'cluster';

const main = React.createClass({
    render() {
        return (
            <div>
                <h1>
                    <Link to='/'>Reduxstahram</Link>
                </h1>
            </div>
        )
    }
})