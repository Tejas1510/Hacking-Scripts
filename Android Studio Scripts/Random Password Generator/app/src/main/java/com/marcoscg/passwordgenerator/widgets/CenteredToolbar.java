package com.marcoscg.passwordgenerator.widgets;

import android.content.Context;
import android.content.res.TypedArray;
import android.support.annotation.Nullable;
import android.support.v7.widget.Toolbar;
import android.util.AttributeSet;
import android.widget.TextView;

public class CenteredToolbar extends Toolbar {

    private TextView titleView;

    public CenteredToolbar(Context context) {
        this(context, null);
    }

    public CenteredToolbar(Context context, @Nullable AttributeSet attrs) {
        this(context, attrs, android.support.v7.appcompat.R.attr.toolbarStyle);
    }

    public CenteredToolbar(Context context, @Nullable AttributeSet attrs, int defStyleAttr) {
        super(context, attrs, defStyleAttr);

        titleView = new TextView(getContext());

        int textAppearanceStyleResId;
        TypedArray a = context.getTheme().obtainStyledAttributes(attrs,
                new int[] { android.support.v7.appcompat.R.attr.titleTextAppearance }, defStyleAttr, 0);
        try {
            textAppearanceStyleResId = a.getResourceId(0, 0);
        } finally {
            a.recycle();
        }
        if (textAppearanceStyleResId > 0) {
            titleView.setTextAppearance(context, textAppearanceStyleResId);
        }

        addView(titleView, new LayoutParams(LayoutParams.WRAP_CONTENT, LayoutParams.WRAP_CONTENT));
    }

    @Override
    protected void onLayout(boolean changed, int l, int t, int r, int b) {
        super.onLayout(changed, l, t, r, b);
        titleView.setX((getWidth() - titleView.getWidth())/2);
    }

    @Override
    public void setTitle(CharSequence title) {
        titleView.setText(title);
    }
}
