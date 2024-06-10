#include <poppler/glib/poppler.h>
#include <cairo.h>
#include <cairo-pdf.h>

void convert_pdf_to_png(const char *pdf_file, const char *png_file) {
    PopplerDocument *document;
    GError *error = NULL;
    document = poppler_document_new_from_file(pdf_file, NULL, &error);

    if (error) {
        g_error("Failed to open PDF file: %s", error->message);
        g_error_free(error);
        return;
    }

    int n_pages = poppler_document_get_n_pages(document);
    if (n_pages == 0) {
        g_error("No pages found in PDF document.");
        g_object_unref(document);
        return;
    }

    PopplerPage *page = poppler_document_get_page(document, 0);
    if (!page) {
        g_error("Failed to get page from PDF document.");
        g_object_unref(document);
        return;
    }

    double width, height;
    poppler_page_get_size(page, &width, &height);

    cairo_surface_t *surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, (int)width, (int)height);
    cairo_t *cr = cairo_create(surface);

    poppler_page_render(page, cr);

    cairo_surface_write_to_png(surface, png_file);

    cairo_destroy(cr);
    cairo_surface_destroy(surface);
    g_object_unref(page);
    g_object_unref(document);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        g_error("Usage: %s <input.pdf> <output.png>", argv[0]);
        return 1;
    }

    const char *pdf_file = argv[1];
    const char *png_file = argv[2];

    convert_pdf_to_png(pdf_file, png_file);

    return 0;
}

