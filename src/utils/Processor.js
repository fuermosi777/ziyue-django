import $ from 'jquery';

export default {
    processPost(body) {
        console.log(body);
        body = body.replace(/[^>]style=".*?"/g, '');
        body = body.replace(/<style>(.|[\r\n])*?<\/style>/g, '');

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
