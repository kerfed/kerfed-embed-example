# kerfed-whitelabel-example

This is an example of how whitelabeled Kerfed instant quoting can be embedded in a static web page once a `shop` is configured. Feel free to reach out to [sales@kerfed.com](mailto:sales@kerfed.com) for help setting up a shop.

## Static Site

This is an extremely simple static site example which you can feel free to fork. 

## Embedding The Quoting Widget

There are two things needed:
1) The `iframe-resizer` Javascript package included as a script. This allows the embedded quoting widget to expand vertically. It can be self hosted, or included from Cloudflare CDN:
```
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/iframe-resizer/4.0.4/iframeResizer.min.js"></script>
```

2) The shop page in an iFrame, and a call to `iFrameResize`. Include the following snippet on the page where you want quoting, changing the URL to match your shop:

```
<div>
  <iframe src="https://kerfed.com/shop/leland" width="100%" frameBorder="0" scrolling="no"></iframe>
  <script>iFrameResize({heightCalculationMethod:'taggedElement'})</script>    
</div>
```




