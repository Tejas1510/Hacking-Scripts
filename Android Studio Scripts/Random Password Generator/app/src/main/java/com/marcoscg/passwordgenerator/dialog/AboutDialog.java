package com.marcoscg.passwordgenerator.dialog;

import android.content.Context;
import android.support.v7.app.AlertDialog;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.text.util.Linkify;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.marcoscg.passwordgenerator.BuildConfig;
import com.marcoscg.passwordgenerator.R;

import java.lang.ref.WeakReference;

import static android.app.Activity.RESULT_OK;

/**
 * A simple about dialog.
 * @author @MarcosCGdev
 */
public class AboutDialog {

    private static WeakReference<Context> contextRef;
    private static AlertDialog.Builder alertDialog;
    private static String authorStr = "Your name", websiteStr = "www.yourwebsite.com";

    public AboutDialog(Context context, String author, String website) {
        contextRef = new WeakReference<Context>(context);
        authorStr = author;
        websiteStr = website;

        init();
    }

    private AboutDialog(AboutDialog.Builder builder) {
        this(builder.context, builder.author, builder.website);
    }

    public void show() {
        if (alertDialog!=null)
            alertDialog.show();
    }

    public static class Builder {

        private Context context;
        private String author = "Your name", website = "www.yourwebsite.com";

        public Builder(Context context) {
            this.context = context;
        }

        public Builder setAuthor(String author) {
            this.author = author;
            return this;
        }

        public Builder setWebsite(String website) {
            this.website = website;
            return this;
        }

        public AboutDialog build() {
            return new AboutDialog(this);
        }

        public void show() {
            new AboutDialog(this).show();
        }

    }

    private static void init() {
        alertDialog = new AlertDialog.Builder(contextRef.get());
        View view = View.inflate(contextRef.get(), R.layout.about_dialog_content, null);
        TextView textView = view.findViewById(R.id.message);

        String message = "<b>Version:</b> " + BuildConfig.VERSION_NAME +
                "<br><b>Author:</b> " + authorStr + "<br><br><b>Website:</b><br>" + websiteStr;

        if (view.getParent()!=null)
            ((ViewGroup)view.getParent()).removeView(view);

        textView.setText(Html.fromHtml(message));
        textView.setAutoLinkMask(RESULT_OK);
        textView.setMovementMethod(LinkMovementMethod.getInstance());
        Linkify.addLinks(textView, Linkify.WEB_URLS);

        alertDialog.setIcon(R.mipmap.ic_launcher);
        alertDialog.setTitle(R.string.about);
        alertDialog.setView(view);
        alertDialog.setPositiveButton(android.R.string.ok, null);
    }

}
