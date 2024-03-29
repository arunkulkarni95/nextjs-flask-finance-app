import './globals.css'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Financial Forecasting App',
  description: 'Full-stack financial forecasting engine',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
      <meta name="google-site-verification" content="l84AIEUse7UuTuKFRxKRnqXwk5Ksjn2K49x6w3KKm1A" />
      </head>
      <body className={inter.className}>{children}</body>
    </html>
  )
}
