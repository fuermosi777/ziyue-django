import React from 'react';
import Styles from './InfoSidebar.less';
import ScrollView from '../ScrollView/ScrollView.jsx';
import Mixpanel from '../../utils/Mixpanel.js';
import {THEMES} from '../../utils/Constant.js';

export default React.createClass({
    propsType: {
        categorys: React.PropTypes.array,
        selectedCategory: React.PropTypes.object,
        onThemeSelected: React.PropTypes.func,
        onReadLaterSelect: React.PropTypes.func,
        readLaterNumber: React.PropTypes.number,
        favNumber: React.PropTypes.number,
        readingMode: React.PropTypes.bool
    },

    getInitialState() {
        return {
            keyword: '',
            isSettingOpen: false,
            isCategoryOpen: true,
            isPersonalOpen: true
        }
    },

    componentWillMount() {
    },

    render() {
        let Categorys = this.props.categorys.map((item, i) => {
            return (
                <li key={i} className={this.props.selectedCategory && this.props.selectedCategory.name === item.name ? 'active' : ''} onClick={this.handleCategoryClick.bind(this, item)}>{item.name}</li>
            );
        });

        let ThemeList = THEMES.map((item, i) => {
            return (
                <li key={i} onClick={this.handleThemeItemClick.bind(this, item)}>{item}</li>
            );
        });

        return (
            <div className={"InfoSidebar " + (this.props.readingMode ? 'reading' : '')}>
                <ScrollView>
                    <div className="InfoSidebar-title" onClick={this.handleDiscoverBtnClick}><i className={this.state.isCategoryOpen ? "ion-android-arrow-dropdown" : "ion-android-arrow-dropright"}></i>发现</div>
                    {this.state.isCategoryOpen ? <ul className="InfoSidebar-categorys animated fadeInLeft">
                        {Categorys}
                    </ul> : ''}

                    <div className="InfoSidebar-title" onClick={this.handlePersonalBtnClick}><i className={this.state.isPersonalOpen ? "ion-android-arrow-dropdown" : "ion-android-arrow-dropright"}></i>个人</div>
                    {this.state.isPersonalOpen ? <ul className="InfoSidebar-categorys animated fadeInLeft">
                        <li onClick={this.handleReadLaterBtnClick}>稍后阅读 <span className="badge">{this.props.readLaterNumber}</span></li>
                        <li onClick={this.handleFavBtnClick}>收藏文章 <span className="badge">{this.props.favNumber}</span></li>
                    </ul> : ''}
                </ScrollView>

                <div className="InfoSidebar-info">
                    <i className={'fa ' + (this.state.isSettingOpen ? 'ion-chevron-down' : 'ion-chevron-up') + ' setting'} onClick={this.handleArrowClick}></i>
                    <span className="name">子阅 ziyue.io</span>
                    <a href="http://about.ziyue.io" target="_blank"><i className="ion-help-circled question"></i></a>
                </div>
                {this.state.isSettingOpen ? 
                    <ul className="InfoSidebar-panel" style={{height: (THEMES.length + 1) * 30}}>
                        <li className="title">选择主题</li>
                        {ThemeList}
                    </ul> 
                : ''}
            </div>
        );
    },

    handleCategoryClick(e) {
        this.handleCategorySelect(e);
        Mixpanel.trackCategoryClickEvent(e.category);
    },

    handleCategorySelect(category) {
        this.props.onCategorySelected(category);
    },

    handleArrowClick() {
        this.setState({'isSettingOpen': !this.state.isSettingOpen});
    },

    handleThemeItemClick(t) {
        this.props.onThemeSelected(t);
    },

    handleDiscoverBtnClick() {
        this.setState({'isCategoryOpen': !this.state.isCategoryOpen});
    },

    handlePersonalBtnClick() {
        this.setState({'isPersonalOpen': !this.state.isPersonalOpen});
    },

    handleReadLaterBtnClick() {
        this.props.onReadLaterSelect();
    },

    handleFavBtnClick() {
        this.props.onFavSelect();
    }
});