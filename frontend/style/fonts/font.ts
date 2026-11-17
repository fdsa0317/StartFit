import localFont from "next/font/local";

const IBMPlexSansKR = localFont({
    src: [
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-ExtraLight.woff2",
            weight: "200",
        },
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-Light.woff2",
            weight: "300",
        },
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-Regular.woff2",
            weight: "400",
        },
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-Medium.woff2",
            weight: "500",
        },
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-SemiBold.woff2",
            weight: "600",
        },
        {
            path: "../../public/assets/fonts/IBMPlexSansKR/IBMPlexSansKR-Bold.woff2",
            weight: "700",
        },
    ],
    display: "swap",
    variable: "--font-IBMPlexSansKR"
})


const outfit = localFont({
    src: [
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-100-normal.woff2",
            weight: "100",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-200-normal.woff2",
            weight: "200",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-300-normal.woff2",
            weight: "300",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-400-normal.woff2",
            weight: "400",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-500-normal.woff2",
            weight: "500",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-600-normal.woff2",
            weight: "600",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-700-normal.woff2",
            weight: "700",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-800-normal.woff2",
            weight: "800",
        },
        {
            path: "../../public/assets/fonts/outfit/outfit-latin-900-normal.woff2",
            weight: "900",
        },
    ],
    display: "swap",
    variable: "--font-outfit"
})



export { IBMPlexSansKR, outfit };
