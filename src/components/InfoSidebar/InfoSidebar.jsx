import React from 'react';
import Styles from './InfoSidebar.less';
import Tracker from '../../utils/Tracker.js';
import {THEMES} from '../../utils/Constant.js';

export default React.createClass({
    propsType: {
        categorys: React.PropTypes.array,
        selectedCategory: React.PropTypes.object,
        onThemeSelected: React.PropTypes.func
    },

    getInitialState() {
        return {
            keyword: '',
            isSettingOpen: false,
            isCategoryOpen: true
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
            <div className="InfoSidebar">
                <div className="InfoSidebar-title" onClick={this.handleDiscoverBtnClick}><i className={this.state.isCategoryOpen ? "ion-android-arrow-dropdown" : "ion-android-arrow-dropright"}></i>发现</div>
                {this.state.isCategoryOpen ? <ul className="InfoSidebar-categorys animated fadeInDown">
                    {Categorys}
                </ul> : ''}

                <div className="InfoSidebar-info">
                    <i className={'fa ' + (this.state.isSettingOpen ? 'ion-chevron-down' : 'ion-chevron-up') + ' setting'} onClick={this.handleArrowClick}></i>
                    <span className="name">子阅 ziyue.io</span>
                    <i className="ion-help-circled question" onClick={this.handleQuestionClick}></i>
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
        Tracker.trackCategoryClickEvent(e.category);
    },

    handleCategorySelect(category) {
        this.props.onCategorySelected(category);
    },

    handleArrowClick() {
        this.setState({'isSettingOpen': !this.state.isSettingOpen});
    },

    handleQuestionClick() {
        window.location.href = "mailto:liuhao1990@gmail.com?subject=意见/建议/问题&body=如有任何疑问，请联系我们吧！";
    },

    handleThemeItemClick(t) {
        this.props.onThemeSelected(t);
    },

    handleDiscoverBtnClick() {
        this.setState({'isCategoryOpen': !this.state.isCategoryOpen});
    }
});