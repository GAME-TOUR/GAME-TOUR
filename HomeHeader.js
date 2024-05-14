import React, { Component } from 'react';
import { connect } from 'react-redux';
import './HomeHeader.scss';
import pubgImage from './pubg.jpg';
import eldenImage from './eldenring.jpg';
import hadesImage from './hades.jpg';
import csgoImage from './csgo.jpg';
import darksoulImage from './darksoul.jpg';
import vrisingImage from './vrising.jpg';
class HomeHeader extends Component {

    render() {

        return (
            <React.Fragment>
                <div className='home-header-container'>
                    <div className='home-header-content'>
                        <div className='left-content'>
                            {/* <i class="fas fa-bars"></i> */}
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

                <div className="home-header-banner">
                    <div className='content-up'>
                        <div className="title1">WELCOME TO GAMETOUR</div>
                        <div className="title2">BEST GAME REVIEW WEBSITE</div>
                        <div className="search">
                            <i className="fas fa-search"></i>
                            <input type="text" placeholder="Find games" />
                        </div>
                    </div>
                    <div className='content-down'>
                        <div className='content-down-text'>POPULAR GAMES</div>
                        <div className="options">
                            <div className='option-child'>
                                <img src={pubgImage} alt="PUBG-Battleground" className='image-child' />
                                <div className='text-child'> PUBG Battleground</div>
                            </div>
                            <div className='option-child'>
                                <img src={eldenImage} alt="elden-Ring" className='image-child' />
                                <div className='text-child'> Elden Ring</div>
                            </div>
                            <div className='option-child'>
                                <img src={hadesImage} alt="Hades" className='image-child' />
                                <div className='text-child'> Hades</div>
                            </div>
                            <div className='option-child'>
                                <img src={csgoImage} alt="CSGO" className='image-child' />
                                <div className='text-child'> CSGO</div>
                            </div>
                            <div className='option-child'>
                                <img src={darksoulImage} alt="Dark-Soul" className='image-child' />
                                <div className='text-child'> Dark Soul</div>
                            </div>
                            <div className='option-child'>
                                <img src={vrisingImage} alt="VRising" className='image-child' />
                                <div className='text-child'> V Rising</div>
                            </div>
                        </div>
                    </div>

                </div>
            </React.Fragment>

        );
    }

}

const mapStateToProps = state => {
    return {
        isLoggedIn: state.admin.isLoggedIn
    };
};

const mapDispatchToProps = dispatch => {
    return {
    };
};

export default connect(mapStateToProps, mapDispatchToProps)(HomeHeader);
