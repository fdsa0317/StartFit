import type { Metadata } from "next";
import "./globals.css";
import "@/style/tailwind/tailwind.theme.css"
import { IBMPlexSansKR } from "@/style/fonts/font";
import { cn } from "@/lib/utils";
import ReactQueryProvider from "@/provider/ReactQueryProvider";
import Header from "./_components/header/Header";
import Footer from "./_components/footer/Footer";
import Main from "./_components/main/Main";


export const metadata: Metadata = {
  title: "우리 프로젝트 타이틀",
  description: "우리 프로젝트 설명"
}

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className={cn(IBMPlexSansKR.variable, "font-sans")}>
      <body className="font-IBMPlexSansKR">
        <ReactQueryProvider>
          <Header />
          <Main />
          {children}
          <Footer />
        </ReactQueryProvider>
      </body>
    </html>
  );
}
