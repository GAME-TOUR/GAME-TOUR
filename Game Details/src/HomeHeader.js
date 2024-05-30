import React, { Component } from 'react';
import './HomeHeader.scss';

class HomeHeader extends Component {
    render() {
        return (
            <React.Fragment>
                <div className='home-header-container'>
                    <div className='home-header-content'>
                        <div className='left-content'>
                            <div className='header-logo'></div>
                        </div>
                        <div className='center-content'>
                            <div className='child-content'>
                                <div><b>Log in</b></div>
                                <div></div>
                            </div>
                            <div className='child-content'>
                                <div><b>Join</b></div>
                                <div></div>
                            </div>
                            <div className='child-content'>
                                <div><b>Games</b></div>
                                <div></div>
                            </div>
                            <div className='child-content'>
                                <div><b>Search</b></div>
                                <div></div>
                            </div>
                        </div>
                        <div className='right-content'>
                            <div className='support'><i class="fas fa-question-circle"></i>Assist</div>
                            <div className='flag'>EN</div>
                        </div>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}

export default HomeHeader;
