import $ from 'jquery';

export default {
    processPost(body) {
        body = body.replace(/[^>]style=".*?"/g, '');
        body = body.replace(/[^>]align=".*?"/g, '');
        body = body.replace(/<style>(.|[\r\n])*?<\/style>/g, '');
        body = body.replace(/<p>(\s|&nbsp;)*?<\/p>/g, '');

        // remove <p><br></p>p> || <section><br></section>section>
        /*
        doc.find('p').each((idx, val) => {
            let $val = $(val);
            if (!!$val.find('br').length && !$val.text().length) {
                $val.remove();
            }
        });
        doc.find('section').each((idx, val) => {
            let $val = $(val);
            if (!!$val.find('br').length && !$val.text().length) {
                $val.remove();
            }
        });


        doc.find('*').removeAttr('style')
            .removeAttr('width')
            .removeAttr('height');
            */

        return body;
    }
};
