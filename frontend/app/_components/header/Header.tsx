
import Image from "next/image";
import Link from "next/link";
import logoDark from "@/public/assets/images/header/logo.svg"
import logoWhite from "@/public/assets/images/header/logo-w.svg"

export default function Header() {
    return (
        <header className="fixed top-0 flex justify-center items-center w-full h-24 bg-[rgba(5,11,23,0.7)] px-[5%] z-10">
            <div className="flex justify-between items-center h-24 w-full max-w-[1440px]">
                <Link href="#">
                    <Image src={logoWhite} alt="" />
                </Link>

                <ul className="flex gap-[30px] text-white font-semibold">
                    <li><Link href="#">서비스 소개</Link></li>
                    <li><Link href="#">상권 분석</Link></li>
                    <li><Link href="#">지원사업 매칭</Link></li>
                    <li><Link href="#">기획서 AI 분석</Link></li>
                    <li><Link href="#">커뮤니티</Link></li>
                </ul>

                <div className="flex gap-[20px] font-bold">
                    <Link 
                        href={"/login"}
                        className="bg-[#5EF0DC] border-1 border-[#fff] rounded-[50px] px-5 py-3 shadow-[5px_3px_20px_1px_rgba(94,240,220,0.3)]"
                    >로그인</Link>
                    <Link 
                        href={"/join"} 
                        className="bg-white border-1 border-[#5EF0DC] rounded-[50px] px-5 py-3"
                    >회원가입</Link>
                </div>
            </div>
        </header>
    );
}