<div align="center">

# SHZv2rayNG

**A customized Android V2Ray client maintained by ShirazTipsy**

![SHZv2rayNG logo](branding/SHZv2rayNG-logo.png)

[English](#english) · [فارسی](#فارسی) · [Latest Release](https://github.com/shiraztest2000-lang/v2rayNG/releases/latest)

[![Latest Release](https://img.shields.io/github/v/release/shiraztest2000-lang/v2rayNG?label=Release)](https://github.com/shiraztest2000-lang/v2rayNG/releases)
[![Downloads](https://img.shields.io/github/downloads/shiraztest2000-lang/v2rayNG/total?logo=github)](https://github.com/shiraztest2000-lang/v2rayNG/releases)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/shiraztest2000-lang/v2rayNG)](https://github.com/shiraztest2000-lang/v2rayNG/commits/master)

</div>

---

## English

### About

**SHZv2rayNG** is an independently maintained fork of [2dust/v2rayNG](https://github.com/2dust/v2rayNG), customized and branded by **ShirazTipsy**. It is an Android client for V2Ray-based connections and supports the cores and protocols provided by the upstream project.

This fork keeps its own application identity, release workflow, and project documentation.

### What's customized in this fork

- **Dedicated app identity:** displayed name `SHZv2rayNG` and a separate Android application ID (`com.v2ray.ang.shz` for the Play Store build), allowing it to be installed alongside the official v2rayNG app.
- **Allow Insecure option:** the TLS `allowInsecure` setting is available in the app's configuration interface. Enabling it disables certificate verification for the relevant connection; use it only when you understand and accept the security implications.
- **ShirazTipsy branding:** the About entry is branded as `ShirazTipsy`, with fork-specific identification in the app interface.
- **Independent releases:** APK names, versioning, and release downloads are maintained in this repository.

### Download

**Current version: `v.2.4.1.001`**

- [Download the latest SHZv2rayNG release](https://github.com/shiraztest2000-lang/v2rayNG/releases/latest)
- [Browse all releases and APK variants](https://github.com/shiraztest2000-lang/v2rayNG/releases)

Choose the APK that matches your device architecture and distribution. The F-Droid build uses its own application ID suffix and can be installed separately from the Play Store build.

### Supported features

SHZv2rayNG is based on v2rayNG and retains its supported connection types and core integrations, including:

- Xray core and v2fly core support, as provided by the upstream project.
- Importing configurations from clipboard, QR code, local files, and supported share links.
- Subscription and profile management.
- Routing and GeoIP/Geosite asset support.
- The fork-specific TLS `Allow Insecure` configuration option.

For core implementation details and upstream changes, see the [original v2rayNG project](https://github.com/2dust/v2rayNG), [Xray-core](https://github.com/XTLS/Xray-core), and [v2fly/v2ray-core](https://github.com/v2fly/v2ray-core).

### GeoIP and Geosite

GeoIP and Geosite data files are managed in the app's assets directory. Updated rule data can be obtained from:

- [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
- [Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip)

A working connection may be required to download rule updates from within the app.

### Development

The Android project is located in the `V2rayNG/` directory and can be opened with Android Studio. Build instructions and CI workflows are maintained in this repository:

- [Source code](https://github.com/shiraztest2000-lang/v2rayNG/tree/master/V2rayNG)
- [Build workflows](https://github.com/shiraztest2000-lang/v2rayNG/tree/master/.github/workflows)
- [Commit history](https://github.com/shiraztest2000-lang/v2rayNG/commits/master)

### Security note

The `Allow Insecure` setting weakens TLS server identity verification and can expose connections to interception. Keep it disabled unless a specific server requires it and you trust that server.

### Project status and attribution

SHZv2rayNG is an **unofficial fork**. It is not the official v2rayNG project and is not affiliated with or endorsed by the upstream maintainers. The upstream project and its contributors retain their respective copyrights and licenses. See [LICENSE](https://github.com/shiraztest2000-lang/v2rayNG/blob/master/LICENSE).

---

## فارسی

### معرفی برنامه

**SHZv2rayNG** نسخه‌ای مستقل و سفارشی‌شده از پروژه متن‌باز [v2rayNG](https://github.com/2dust/v2rayNG) است که با برند **ShirazTipsy** توسعه و نگهداری می‌شود. این برنامه یک کلاینت اندرویدی برای اتصال‌های مبتنی بر V2Ray است و قابلیت‌های هسته‌ای پروژه اصلی را حفظ می‌کند.

این فورک نام، شناسه نصب، روند انتشار نسخه‌ها و مستندات اختصاصی خودش را دارد.

### تغییرات اختصاصی این فورک

- **هویت مستقل برنامه:** نام نمایشی برنامه `SHZv2rayNG` است و شناسه نصب نسخه Play Store به `com.v2ray.ang.shz` تغییر کرده است؛ بنابراین امکان نصب در کنار نسخه رسمی v2rayNG وجود دارد.
- **قابلیت Allow Insecure:** گزینه تنظیم `allowInsecure` مربوط به TLS در رابط تنظیمات برنامه در دسترس است. فعال‌کردن آن بررسی گواهی TLS را برای اتصال مربوطه غیرفعال می‌کند؛ این گزینه فقط در صورت آگاهی از پیامدهای امنیتی و اعتماد به سرور فعال شود.
- **برند ShirazTipsy:** بخش About با عنوان `ShirazTipsy` مشخص شده و هویت فورک در رابط برنامه نمایش داده می‌شود.
- **انتشار مستقل:** نام فایل‌های APK، شماره نسخه و فایل‌های انتشار از همین مخزن مدیریت می‌شوند.

### دانلود

**نسخه فعلی: `v.2.4.1.001`**

- [دانلود آخرین نسخه SHZv2rayNG](https://github.com/shiraztest2000-lang/v2rayNG/releases/latest)
- [مشاهده تمام نسخه‌ها و فایل‌های APK](https://github.com/shiraztest2000-lang/v2rayNG/releases)

هنگام دانلود، فایل متناسب با معماری پردازنده دستگاه و نوع توزیع را انتخاب کنید. نسخه F-Droid شناسه نصب جداگانه‌ای دارد و می‌تواند در کنار نسخه Play Store نصب شود.

### قابلیت‌ها

SHZv2rayNG بر پایه v2rayNG ساخته شده و قابلیت‌های اتصال و هسته‌های پشتیبانی‌شده در پروژه اصلی را حفظ می‌کند؛ از جمله:

- پشتیبانی از هسته‌های Xray و v2fly مطابق پروژه اصلی.
- افزودن کانفیگ از کلیپ‌بورد، QR Code، فایل محلی و لینک‌های اشتراک پشتیبانی‌شده.
- مدیریت پروفایل‌ها و اشتراک‌ها.
- تنظیمات مسیریابی و پشتیبانی از فایل‌های GeoIP و Geosite.
- گزینه اختصاصی `Allow Insecure` برای تنظیمات TLS.

برای اطلاعات فنی بیشتر درباره هسته‌ها و تغییرات پروژه مادر، به مخازن [v2rayNG اصلی](https://github.com/2dust/v2rayNG)، [Xray-core](https://github.com/XTLS/Xray-core) و [v2fly/v2ray-core](https://github.com/v2fly/v2ray-core) مراجعه کنید.

### فایل‌های GeoIP و Geosite

فایل‌های داده GeoIP و Geosite در پوشه دارایی‌های برنامه نگهداری می‌شوند. برای دریافت داده‌های به‌روز می‌توانید از منابع زیر استفاده کنید:

- [Loyalsoldier/v2ray-rules-dat](https://github.com/Loyalsoldier/v2ray-rules-dat)
- [Loyalsoldier/geoip](https://github.com/Loyalsoldier/geoip)

برای دریافت فایل‌های به‌روزرسانی از داخل برنامه ممکن است به یک اتصال فعال نیاز داشته باشید.

### توسعه و کد منبع

پروژه اندروید در پوشه `V2rayNG/` قرار دارد و با Android Studio قابل بازکردن است:

- [مشاهده کد منبع](https://github.com/shiraztest2000-lang/v2rayNG/tree/master/V2rayNG)
- [فایل‌های ساخت و گردش‌کارها](https://github.com/shiraztest2000-lang/v2rayNG/tree/master/.github/workflows)
- [تاریخچه تغییرات](https://github.com/shiraztest2000-lang/v2rayNG/commits/master)

### نکته امنیتی

فعال‌کردن `Allow Insecure` اعتبارسنجی هویت سرور در TLS را تضعیف می‌کند و می‌تواند خطر رهگیری ارتباط را افزایش دهد. این گزینه را فقط زمانی فعال کنید که سرور مشخصی به آن نیاز دارد و به آن سرور اعتماد دارید.

### وضعیت پروژه و حقوق

SHZv2rayNG یک **فورک غیررسمی** است؛ پروژه رسمی v2rayNG نیست و وابستگی یا تأیید رسمی از سوی توسعه‌دهندگان پروژه مادر ندارد. حقوق و مجوزهای کد اصلی متعلق به صاحبان و مشارکت‌کنندگان آن پروژه است. متن مجوز در فایل [LICENSE](https://github.com/shiraztest2000-lang/v2rayNG/blob/master/LICENSE) قرار دارد.

---

<div align="center">

**SHZv2rayNG · Maintained by ShirazTipsy**

[Repository](https://github.com/shiraztest2000-lang/v2rayNG) · [Releases](https://github.com/shiraztest2000-lang/v2rayNG/releases) · [Issues](https://github.com/shiraztest2000-lang/v2rayNG/issues)

</div>
